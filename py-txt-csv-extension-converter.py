"""
Script: File Extension Modifier
Description: This Python script allows you to add or remove the '.csv' or '.txt' file extension for files in the same directory as the script. Files with a '.py' extension will be ignored.

Requirements:
- Python 3.x
- Place this script in the same directory as the files you want to modify.

Usage:
1. Run the script.
2. Choose whether to add or remove an extension.
3. Specify the extension you want to add or remove ('csv' or 'txt').

Created by Jonas Lund in 2023.
"""

import os

# Get the current directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# List all files in the script's directory
file_list = os.listdir(script_directory)

# Function to add or remove a file extension
def modify_extension(file_name, new_extension):
    base_name, _ = os.path.splitext(file_name)
    new_file_name = base_name + new_extension
    os.rename(os.path.join(script_directory, file_name), os.path.join(script_directory, new_file_name))

# Ask the user whether to add or remove the extension
action = input("Do you want to add or remove an extension? (add/remove): ").strip().lower()

if action == 'add' or action == 'remove':
    extension_choice = input("Which extension do you want to modify? (csv/txt): ").strip().lower()
    
    if extension_choice == 'csv' or extension_choice == 'txt':
        target_extension = '.' + extension_choice
        # Perform the chosen action for each file
        for file_name in file_list:
            if file_name.endswith('.py'):
                continue  # Ignore files with .py extension
            current_extension = os.path.splitext(file_name)[1].lower()
            if action == 'add':
                if not current_extension:
                    modify_extension(file_name, target_extension)
                    print(f"Added '.{extension_choice}' extension to '{file_name}'")
            elif action == 'remove' and current_extension == target_extension:
                modify_extension(file_name, '')
                print(f"Removed '.{extension_choice}' extension from '{file_name}'")
    else:
        print("Invalid extension choice. Please enter 'csv' or 'txt'.")
else:
    print("Invalid choice. Please enter 'add' or 'remove'.")

print(f"Finished the '{action}' operation for '{extension_choice}' files in the script's directory.")
