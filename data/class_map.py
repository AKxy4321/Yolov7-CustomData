import os


def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, "r") as file:
        file_content = file.read()

    file_content = file_content.replace(old_text.strip(), new_text.strip())

    with open(file_path, "w") as file:
        file.write(file_content)


def process_directory(directory_path, old_text, new_text):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path = os.path.join(root, file_name)
                replace_text_in_file(file_path, old_text, new_text)
                print(f"Processed: {file_path}")


# Directory containing the text files
directory_path = "./yolo"

# Old text to be replaced
old_text = "1"

# New text
new_text = "0"

# Process the directory
process_directory(directory_path, old_text, new_text)
