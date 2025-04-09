# Description: This script generates distractors for a given problem and creates a Moodle XML file with the problem and distractors.
import os
import json
import ast
import xml.sax.saxutils

USE_AI_DISTRACTORS = False  # Set to False to disable AI distractor generation

if USE_AI_DISTRACTORS:
    import openai
    client = openai.OpenAI()

def escape_xml(text):
    return xml.sax.saxutils.escape(str(text))

def generate_distractors(problem):
    if not USE_AI_DISTRACTORS:
        return ["Distractor 1", "Distractor 2", "Distractor 3", "Distractor 4"]  # Default placeholders
    
    prompt = f"""Return a list of four strings elements (use double quotes) where each string is a distractor for this problem (format as [<str>,<str>,...]):
    {problem}"""
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        raw_text = completion.choices[0].message.content
        return ast.literal_eval(raw_text)
    except Exception as e:
        print(f"Error generating distractors: {e}")
        return ["Fallback Distractor 1", "Fallback Distractor 2", 
                "Fallback Distractor 3", "Fallback Distractor 4"]

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
    # Extract and validate fields
    title = escape_xml(problem_data.get("title", "Untitled Question"))
    
    question_text = problem_data.get("question_text", "No question text provided.")
    image_url = problem_data.get("image_url")
    if image_url:
        question_text += f'<img src="{escape_xml(image_url)}" width="400" />'
    else:
        question_text += "<p>No image provided.</p>"
    question_text = math_format(question_text)
    
    solution_data = problem_data.get("solution", {})
    final_answer = solution_data.get("final_answer", "No Correct Answer")
    final_answer = math_format(final_answer)
    
    # Process distractors
    processed_distractors = [escape_xml(math_format(d)) for d in distractors][:4]  # Ensure max 4 distractors

    # Build XML
    xml_str = f"""<?xml version="1.0"?>
<quiz>
  <question type="category">
    <category>
      <text>OWLet 1 (for Unit 1: Introduction)</text>
    </category>
  </question>
  
  <question type="multichoice">
    <name>
      <text>{title}</text>
    </name>
    <questiontext format="html">
      <text><![CDATA[<p>{question_text}</p>]]></text>
    </questiontext>
    <generalfeedback format="html">
      <text><![CDATA[]]></text>
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
    
    <answer fraction="100" format="html">
      <text><![CDATA[<p>{final_answer}</p>]]></text>
    </answer>
"""

    for distractor in processed_distractors:
        xml_str += f"""
    <answer fraction="0" format="html">
      <text><![CDATA[<p>{distractor}</p>]]></text>
    </answer>
"""
    xml_str += """
  </question>
</quiz>
"""
    return xml_str

# Main execution
with open("input.json", "r", encoding="utf-8") as f:
    problem_data = json.load(f)

distractors = generate_distractors(problem_data)
xml_content = create_moodle_xml(problem_data, distractors)

with open("output.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)
