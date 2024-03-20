import os

# Directory containing images and annotations
image_dir = "./images"
annotation_dir = "./labels"


# Function to read annotation files
def read_annotation_file(annotation_file):
    with open(annotation_file, "r") as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]


# Function to write annotation files
def write_annotation_file(annotation_file, lines):
    with open(annotation_file, "w") as file:
        for line in lines:
            file.write(" ".join(line) + "\n")


# List image and annotation files
image_files = os.listdir(image_dir)
annotation_files = os.listdir(annotation_dir)

# Iterate over annotation files
for annotation_file in annotation_files:
    if annotation_file.endswith(".txt"):
        image_name = os.path.splitext(annotation_file)[0] + ".jpg"
        image_path = os.path.join(image_dir, image_name)
        annotation_path = os.path.join(annotation_dir, annotation_file)

        # Read annotation file
        annotations = read_annotation_file(annotation_path)

        # Check if class 1 annotations exist
        class_1_exist = any(int(label[0]) == 1 for label in annotations)

        if not class_1_exist:
            # Remove annotation file
            os.remove(annotation_path)

            # Remove corresponding image file
            if os.path.exists(image_path):
                os.remove(image_path)
        else:
            # Remove annotations of other classes
            for label in annotations:
                if int(label[0]) != 1:
                    annotations.remove(label)

            # Write updated annotation file
            write_annotation_file(annotation_path, annotations)
