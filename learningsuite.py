#writing stuff
import os
import openai
import json
import ast


client = openai.OpenAI()


#writing
def generate_distractors(problem):
    prompt= f"""return a list of four strings elements (don't forget double quotes around each string!) where each string is a distractor for the following problem (given in this format e.g. [<str>,<str>,...], do not include ticmarks or a code environment just the list).  distractors should be of teh same format as the final answer
    ): \n + {problem}"""
    try:
        # Combine the solicitation segment, template, and context to form the prompt

        # Generate the completion using the client
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the generated text from the completion result
        raw_generated_text = completion.choices[0].message.content
        print( raw_generated_text)
        generated_text = ast.literal_eval( raw_generated_text)
    except Exception as e:
        print(f"An error occurred in the text generator: {e}")
        generated_text = "Error: Could not generate the paragraph."

    return generated_text


def math_format(text: str):
    result = text

    # Split text by '$$' and use list comprehension to add <span> and </span> alternatively.
    parts = result.split('$$')
    # Join the parts with alternating <span> and </span> tags.
    result = ''.join(
        rf'<span class="math-tex">\({part}\)</span>' if i % 2 == 1 else part
        for i, part in enumerate(parts)
    )
    return result


def create_moodle_xml(problem_data, distractors):
    """
    Creates a Moodle XML string for a multiple-choice question based on:
      - A required category block
      - A 'multichoice' question block
      - The correct answer
      - Distractors (incorrect answers)

    :param problem_data: Dictionary loaded from your JSON file.
    :return: A string of well-formed Moodle XML.
    """
    distractors = [math_format(distractor) for distractor in distractors]
    # Extract the fields we need from the JSON
    title = problem_data.get("title", "Untitled Question")
    
    question_text = problem_data.get("question_text", "No question text provided.")
    question_text += f'<img src="{problem_data.get("image_url")}" width="400" /><br />'
    question_text = math_format(question_text)
    
    solution_data = problem_data.get("solution", {})
    
    final_answer = solution_data.get("final_answer", "No Correct Answer")
    final_answer = math_format(final_answer)
    
    steps = solution_data.get("steps", [])
    steps = [math_format(step) for step in steps]

    # Combine steps into a single string for feedback (you can customize formatting)
    steps_feedback = "<br/>".join(steps)
    steps_feedback += f'<img src="{problem_data.get("solution_url")}" width="400" /><br />'
    steps_feedback = math_format(steps_feedback)

    # Note: This template is based on your "corrected XML" structure,
    #       adjusting only what is necessary to incorporate your question/answer content.
    xml_str = f"""<?xml version="1.0"?>
        <quiz>
        <!-- Category for the question -->
        <question type="category">
            <category>
            <text>OWLet 1 (for Unit 1: Introduction)</text>
            </category>
        </question>
        
        <!-- Start of the multiple-choice question -->
        <question type="multichoice">
            <name>
            <text>{title}</text>
            </name>
            <questiontext format="html">
            <text><![CDATA[<p>{question_text}</p>]]></text>
            </questiontext>
            <generalfeedback format="html">
            <text><![CDATA[<p></p>]]></text>
            </generalfeedback>
            <penalty>0.3333333</penalty>
            <hidden>0</hidden>
            <defaultgrade>1</defaultgrade>
            <single>1</single>
            <shuffleanswers>false</shuffleanswers>
            <answernumbering>abc</answernumbering>
            
            <correctfeedback format="html">
            <text/>
            </correctfeedback>
            <partiallycorrectfeedback format="html">
            <text/>
            </partiallycorrectfeedback>
            <incorrectfeedback format="html">
            <text/>
            </incorrectfeedback>
            <shownumcorrect/>
            
            <!-- Correct Answer -->
            <answer fraction="100" format="html">
            <text><![CDATA[<p>{final_answer}</p>]]></text>
            <feedback format="html">
                <text><![CDATA[<p>{steps_feedback}</p>]]></text>
            </feedback>
            </answer>
        """

    # Loop over all distractors to create the incorrect answers
    for distractor in distractors:
    
        xml_str += f"""
        <answer fraction="0" format="html">
        <text><![CDATA[<p>{distractor}</p>]]></text>
        <feedback format="html">
            <text><![CDATA[<p>{steps_feedback}</p>]]></text>
        </feedback>
        </answer>
        """

    # Close the question and quiz tags
    xml_str += """
        </question>
        </quiz>
        """
    return xml_str





#call functions
# Load JSON
with open("input.json", "r", encoding="utf-8") as f:
    problem_data = json.load(f)

distractors = generate_distractors(problem_data)

# Generate Moodle XML
xml_content = create_moodle_xml(problem_data, distractors)

# Save to file
with open("output.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)





