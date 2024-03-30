import os

def read_ground_truth_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    return lines

def create_labels_folder(ground_truth_file, images_folder, labels_folder):
    # Read the large ground truth file
    ground_truth_lines = read_ground_truth_file(ground_truth_file)

    current_class = None
    current_image_lines = None

    for line in ground_truth_lines:
        # Extract class and image information
        if line.endswith(".jpg"):
            current_class, image_name = os.path.split(line)
            current_class = os.path.basename(os.path.normpath(current_class))

            # Create the labels directory for the current class if it doesn't exist
            class_labels_folder = os.path.join(labels_folder, current_class)
            os.makedirs(class_labels_folder, exist_ok=True)

            # Open a new label file for the current image
            current_image_lines = []
        elif current_image_lines is not None:
            # Add bounding box information to the current image
            current_image_lines.append(line)

            # If the line is the last bounding box, write the label file
            if line.isdigit() and int(line) == len(current_image_lines) - 1:
                image_path = os.path.join(images_folder, current_class, image_name)
                label_file_path = os.path.join(class_labels_folder, os.path.splitext(image_name)[0] + ".txt")

                with open(label_file_path, 'w') as label_file:
                    label_file.write('\n'.join(current_image_lines))

if __name__ == "__main__":
    ground_truth_file = "txt.txt"
    images_folder = "/path/to/train/images"
    labels_folder = "/path/to/train/labels"

    create_labels_folder(ground_truth_file, images_folder, labels_folder)
