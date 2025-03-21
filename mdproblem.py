import json
import pyperclip  # Make sure to install this via "pip install pyperclip"

def unroll_json(json_chunk, prefix=""):
    # [Your existing unroll_json function code]
    unrolled_text = ""
    for key, value in json_chunk.items():
        formatted_key = f"{prefix}{key.capitalize()}: "
        if isinstance(value, dict):
            nested_prefix = prefix + key.capitalize() + " - "
            unrolled_text += unroll_json(value, nested_prefix)
        else:
            unrolled_text += f"{formatted_key}{value}\n"
    return unrolled_text

def generate_markdown_problem(problem):
    markdown = f"""
### Problem {problem['id']}
**{problem['title']}**
"""
    if "insight" in problem:
        markdown += f'*Insight*: {problem["insight"]}\n\n'
    markdown += f'**Question**: {problem["question_text"]}\n\n'
    if "image_url" in problem:
        markdown += f'\n<img src="{problem["image_url"]}" alt="Alt Text" width="200" height="133">\n'
    markdown += "\n---\n"
    return markdown

def generate_markdown_solution(problem):
    solution = problem["solution"]
    markdown = f"""
### Solution for Problem {problem['id']}
"""
    if "solution_url" in problem:
        markdown += f'<img src="{problem["solution_url"]}" alt="Alt Text" width="200" height="133">\n\n'
    markdown += f'**Answer**: {solution.get("final_answer", "No answer provided")}\n\n'
    if "steps" in solution:
        markdown += "**Steps:**\n"
        for i, step in enumerate(solution["steps"], start=1):
            markdown += f"\n{i}. {step}"
    markdown += "\n\n---\n"
    return markdown

# Read the JSON data from input.json
with open('input.json', 'r') as file:
    problem_data_list = json.load(file)

if not isinstance(problem_data_list, list):
    problem_data_list = [problem_data_list]

# Initialize a variable to collect all markdown content
full_markdown = ""

# Open an output file for writing the Markdown content
with open('output.md', 'w') as output_file:
    for problem_data in problem_data_list:
        problem_markdown = generate_markdown_problem(problem_data)
        solution_markdown = generate_markdown_solution(problem_data)
        full_markdown += problem_markdown + solution_markdown
        output_file.write(problem_markdown)
        output_file.write(solution_markdown)

# Copy the full markdown content to the clipboard
pyperclip.copy(full_markdown)
print("Markdown content has been written to 'output.md' and copied to your clipboard.")
