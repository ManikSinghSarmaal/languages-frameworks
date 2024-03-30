import os

input_file_path = 'modified_file_val.txt'
output_folder = 'labels_val'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

with open(input_file_path, 'r') as file:
    lines = file.readlines()

current_folder = None
current_lines = []

for line in lines:
    # Strip the newline character from each line
    line = line.strip()

    # Check if the line is a folder line (ending with '.jpg')
    if line.endswith('.jpg'):
        # Save the previous folder's data to separate text files
        if current_folder is not None:
            output_folder_path = os.path.join(output_folder, current_folder)
            os.makedirs(output_folder_path, exist_ok=True)
            output_file_path = os.path.join(output_folder_path, os.path.basename(current_image) + '.txt')
            with open(output_file_path, 'w') as output_file:
                output_file.write('\n'.join(current_lines))

        # Start a new folder and reset the lines
        current_folder = line.split('/')[0]
        current_image = line
        current_lines = []
    else:
        # Append the line to the current_lines list
        current_lines.append(line)

# Save the last folder's data to a separate text file
if current_folder is not None:
    output_folder_path = os.path.join(output_folder, current_folder)
    os.makedirs(output_folder_path, exist_ok=True)
    output_file_path = os.path.join(output_folder_path, os.path.basename(current_image) + '.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(current_lines))

print(f"Text files saved in the '{output_folder}' folder.")
