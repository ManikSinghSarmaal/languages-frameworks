import os
import shutil

root_dir = "/Users/maniksinghsarmaal/Downloads/widerface_copy/test/images"  # Replace with the actual path to your root directory
new_dir = "/Users/maniksinghsarmaal/Downloads/img"  # Replace with the desired path for the "All_Images" folder

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith((".jpg", ".jpeg")):  # Only move JPEG images
            file_path = os.path.join(subdir, file)
            shutil.copy(file_path, new_dir)

print("Images moved successfully!")
