import json
import os

# Paths
question_file = "questions/driver_test_ca_bc.json"
output_dir = "source/driver_test/ca/bc"

# Function to write a single question to an `.rst` file
def write_question_rst(question, output_dir, total_questions, language):
    question_id = f"q{question['id']}"  # Unique ID for the question
    filename = f"{question_id}.rst"
    filepath = os.path.join(output_dir, filename)

    # Determine the previous and next question IDs
    prev_question = f"q{question['id'] - 1}" if question['id'] > 1 else None
    next_question = f"q{question['id'] + 1}" if question['id'] < total_questions else None

    # Button text based on language
    if language == "zh":
        prev_text = "上一题"
        next_text = "下一题"
    else:
        prev_text = "Previous Question"
        next_text = "Next Question"

    # Write question content
    with open(filepath, "w", encoding="utf-8") as f:
        # Write meta information for SEO
        write_meta(f, question['question'], question.get("meta_keywords", ""))  # Use question for description

        # Write question number as standalone title
        question_number = f"{question['id']}"
        write_title(f, question_number)

        # Write question in bold
        f.write(f"**{question['question']}**\n\n")

        # Write options with interactive buttons
        write_interactive_html(f, question_id, question['options'], question['answer'])

        # Write explanation (hidden by default)
        f.write("\n.. dropdown:: Explanation\n\n")
        f.write(f"   {question['explanation']}\n")

        # Add navigation buttons
        f.write("\n.. raw:: html\n\n")
        if prev_question is None and next_question:  # Only "Next Question" exists
            f.write("   <div class=\"nav-buttons single-next\">\n")
        else:
            f.write("   <div class=\"nav-buttons\">\n")

        if prev_question:
            f.write(f"       <a href=\"{prev_question}.html\" class=\"button\">{prev_text}</a>\n")
        if next_question:
            f.write(f"       <a href=\"{next_question}.html\" class=\"button\">{next_text}</a>\n")
        f.write("   </div>\n\n")


# Function to write meta information for SEO
def write_meta(file, description, keywords):
    file.write(".. meta::\n")
    file.write(f"   :description: {description}\n")
    file.write(f"   :keywords: {keywords}\n\n")

# Function to write the title with underline
def write_title(file, title):
    file.write(f"{title}\n")
    file.write("=" * (len(title) * 2) + "\n\n")

# Function to write interactive HTML content
def write_interactive_html(file, question_id, options, correct_answer):
    file.write(".. raw:: html\n\n")
    file.write(f"   <div id=\"{question_id}\" class=\"quiz\" data-correct-answer=\"{correct_answer}\">\n")
    for option in options:
        file.write(
            f"       <button onclick=\"checkAnswer('{question_id}', '{option}')\">{option}</button>\n"
        )
    file.write(f"       <p id=\"{question_id}-result\" class=\"result\"></p>\n")
    file.write("   </div>\n\n")

# Function to update the index.rst file with a toctree
def update_toctree(title, questions, output_dir):
    index_path = os.path.join(output_dir, "index.rst")
    with open(index_path, "w", encoding="utf-8") as index_file:
        # Write the title and its underline
        index_file.write(f"{title}\n")
        index_file.write("=" * (len(title)*2) + "\n\n")

        # Write the toctree
        index_file.write(".. toctree::\n")
        index_file.write("   :maxdepth: 2\n\n")
        for question in questions:
            question_id = f"q{question['id']}"
            index_file.write(f"   {question_id}\n")


# Main script logic
def main():
    # Load questions from JSON
    with open(question_file, "r", encoding="utf-8") as f:
        data = json.load(f)  # Load the entire JSON file

    # Extract questions and title
    questions = data["questions"]
    title = data.get("title", "Questions")  # Default title if not provided
    total_questions = len(questions)

    # Determine language (default to Chinese)
    language = "zh"  # Adjust this to "en" for English

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate `.rst` files for each question
    for question in questions:
        write_question_rst(question, output_dir, total_questions, language)  # Pass language here

    # Update the toctree in the index.rst file with the title
    update_toctree(title, questions, output_dir)


if __name__ == "__main__":
    main()
