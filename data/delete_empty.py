import os

def delete_images_without_annotations(images_dir, annotations_dir):
    # Get a list of image files
    image_files = os.listdir(images_dir)

    # Iterate over each image file
    for image_file in image_files:
        # Get the corresponding annotation file name
        annotation_file = os.path.splitext(image_file)[0] + '.txt'
        annotation_path = os.path.join(annotations_dir, annotation_file)

        # Check if the annotation file exists
        if not os.path.exists(annotation_path):
            # If the annotation file doesn't exist, delete the image file
            image_path = os.path.join(images_dir, image_file)
            os.remove(image_path)
            print(f"Deleted {image_path} because corresponding annotation file doesn't exist.")

# Set the paths to your images and annotations folders
images_folder = 'images'
annotations_folder = 'labels'

# Call the function to delete images without annotations
delete_images_without_annotations(images_folder, annotations_folder)
