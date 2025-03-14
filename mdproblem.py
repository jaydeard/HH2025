import json

def unroll_json(json_chunk, prefix=""):
    """
    Unrolls a nested dictionary into a formatted string representation.

    Args:
        json_chunk (dict): The dictionary to be unrolled.
        prefix (str): A prefix to add to each key (for nested contexts).

    Returns:
        str: A formatted string representation of the dictionary.
    """
    unrolled_text = ""
    
    for key, value in json_chunk.items():
        # Capitalize the key and append the prefix if provided
        formatted_key = f"{prefix}{key.capitalize()}: "

        if isinstance(value, dict):
            # Recursively call unroll_context for nested dictionaries
            nested_prefix = prefix + key.capitalize() + " - "
            unrolled_text += unroll_json(value, nested_prefix)
        else:
            # Add the key-value pair to the unrolled text
            unrolled_text += f"{formatted_key}{value}\n"

    return unrolled_text


# Generate markdown for problem statement
def generate_markdown_problem(problem):

    markdown = f"""
### Problem {problem['id']}
**{problem['title']}**
"""
    if "insight" in problem:
        markdown += f'*Insight*: {problem['insight']}\n\n'

    markdown += f"**Question**: {problem["question_text"]}\n\n"
    # Check if image_url exists before adding it
    if "image_url" in problem:
        markdown += f'\n<img src="{problem["image_url"]}" alt="Alt Text" width="200" height="133">\n'

    markdown += "\n---\n"
    return markdown

# Generate markdown for solution
def generate_markdown_solution(problem):
    solution = problem["solution"]
    markdown = f"""
### Solution for Problem {problem['id']}
"""

    if "solution_url" in problem:
        markdown += f'<img src="{problem["solution_url"]}" alt="Alt Text" width="200" height="133">\n\n'

    markdown += f"**Answer**: {solution.get('final_answer', 'No answer provided')}\n\n"

    if "steps" in solution:
        markdown += "**Steps:**\n"
        for i, step in enumerate(solution['steps'], start=1):
            markdown += f"\n{i}. {step}"

    markdown += "\n\n---\n"
    return markdown



# Generate and print the markdown content

with open('input.json', 'r') as file:
    problem_data_list = json.load(file)

if not isinstance(problem_data_list, list):
    problem_data_list = [problem_data_list]

# Open an output file for writing the Markdown content
with open('output.md', 'w') as output_file:
    for problem_data in problem_data_list:
        problem_markdown = generate_markdown_problem(problem_data)
        solution_markdown = generate_markdown_solution(problem_data)

        # Write the markdown content to the file
        output_file.write(problem_markdown)
        output_file.write(solution_markdown)

