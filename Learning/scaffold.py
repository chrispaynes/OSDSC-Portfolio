


import os


# List of strings
file_names = [

]

# Directory to save Markdown files
output_directory = "/Users/chris/code/OSDSC/Learning/Trigonometry"

# Ensure the output directory exists, create if not
os.makedirs(output_directory, exist_ok=True)

# Loop through the list and create empty Markdown files
for file_name in file_names:
    file_path = os.path.join(output_directory, f"{file_name}.md")

    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists.")
        continue

    with open(file_path, "w") as file:
        # Writing an empty file
        pass

print("Markdown files created successfully.")
