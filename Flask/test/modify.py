input_file_path = 'txt.txt'
output_file_path = 'modified_file_val.txt'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

modified_lines = []

skip_line = False

for line in lines:
    if skip_line:
        # Skip the line immediately following the one that ends with '.jpg'
        skip_line = False
        continue

    if line.endswith('.jpg\n'):
        # If the line ends with '.jpg', keep it in the modified lines list
        modified_lines.append(line)
        # Set the flag to skip the next line
        skip_line = True
    else:
        # For all other lines (including bounding box information), keep them in the modified lines list
        modified_lines.append(line)

# Write the modified lines to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)

print(f"Number of bounding boxes removed. Result saved in {output_file_path}")
