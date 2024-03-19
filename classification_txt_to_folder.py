import os
import sys
import shutil
from pathlib import Path

# run the programm like this:
# python classification_txt_to_folder.py <path-to-annotation-file> <path-to-image-folder>
dataset_dir = Path(sys.argv[1])
annotations_file_path = dataset_dir / "classification-annotations.txt"
images_folder_path = dataset_dir / "classification_raw"
save_dir = dataset_dir / "classification_sorted"
save_dir.mkdir(exist_ok=True)

# Read annotations and organize them into a dictionary
annotations = {}
with annotations_file_path.open('r') as file:
    for line in file:
        filename, class_name = line.strip().split(' => ')
        annotations[filename] = class_name

#print(annotations)

# Create a directory for each class and move the corresponding images
for filename, class_name in annotations.items():
    src_path = images_folder_path / filename

    class_folder_path = save_dir / class_name
    class_folder_path.mkdir(exist_ok=True)
    dst_path = class_folder_path / filename
    
    # Move the file
    if os.path.exists(src_path):  # Check if source file exists
        shutil.copy(src_path, dst_path)
    else:
        print(f"File {filename} does not exist and cannot be moved.")

print("Image organization by class completed.")
