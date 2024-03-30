
import os 
input_file = "/Users/maniksinghsarmaal/Downloads/flask/test/modified_file.txt"
output_file = "/Users/maniksinghsarmaal/Downloads/flask/test/updated_file.txt"

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        # Split the line into class and bounding box information
        class_and_bounding_box = line.split("/")
        
        # Ensure the line has the expected format
        if len(class_and_bounding_box) == 2:
            class_info = class_and_bounding_box[0].split("--")
            
            # Extract the class label and bounding box information
            class_label = class_info[0]
            file_name = class_info[1].strip()
            bounding_box_info = class_and_bounding_box[1].strip()

            # Write the updated line to the output file
            f_out.write(f"{file_name}\n{class_label} {bounding_box_info}\n")
        else:
            # If the line doesn't have the expected format, write it unchanged
            f_out.write(line)

