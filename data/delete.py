import os

# Path to your images and labels folders
images_folder = "path/to/your/images/folder"
labels_folder = "path/to/your/labels/folder"

# Get the list of images and labels
image_files = os.listdir(images_folder)
label_files = os.listdir(labels_folder)

# Extract the base filenames without extensions
image_names = [os.path.splitext(file)[0] for file in image_files]
label_names = [os.path.splitext(file)[0] for file in label_files]

# Find images without corresponding labels
images_without_labels = set(image_names) - set(label_names)

# Delete images without labels
for image_name in images_without_labels:
    image_path = os.path.join(images_folder, image_name + ".jpg")  # assuming jpg extension, change if different
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted: {image_path}")
    else:
        print(f"Image not found: {image_path}")

