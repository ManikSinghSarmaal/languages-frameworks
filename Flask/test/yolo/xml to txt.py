
import os
import xml.etree.ElementTree as ET

def xml_to_yolo(xml_file, txt_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    image_width = int(root.find('size').find('width').text)
    image_height = int(root.find('size').find('height').text)

    with open(txt_file, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            # Extract class ID from the filename
            filename = os.path.basename(xml_file)
            class_id = int(filename.split('_')[0])  # Assuming class ID is the first part of the filename

            xmin = int(obj.find('bndbox').find('xmin').text)
            ymin = int(obj.find('bndbox').find('ymin').text)
            xmax = int(obj.find('bndbox').find('xmax').text)
            ymax = int(obj.find('bndbox').find('ymax').text)

            center_x = (xmin + xmax) / 2 / image_width
            center_y = (ymin + ymax) / 2 / image_height
            width = (xmax - xmin) / image_width
            height = (ymax - ymin) / image_height

            f.write(f"{class_id} {center_x} {center_y} {width} {height}\n")

# Get the current directory
current_dir = '/Users/maniksinghsarmaal/Downloads/wider-face-pascal-voc-annotations/WIDER_val_annotations'

# Create a new folder for the TXT files
new_dir = os.path.join(current_dir, "yolo_txt")
os.makedirs(new_dir, exist_ok=True)

# Loop through all files in the current directory
for filename in os.listdir(current_dir):
    if filename.endswith(".xml"):
        # Get the base filename without extension
        base_filename = os.path.splitext(filename)[0]

        # Create the corresponding TXT file path
        txt_file = os.path.join(new_dir, f"{base_filename}.txt")

        # Convert the XML file to TXT
        xml_to_yolo(os.path.join(current_dir, filename), txt_file)

print(f"Converted all XML files to TXT in the '{new_dir}' folder.")

