import xml.etree.ElementTree as ET
import os


def xml_to_yolo(xml_path, image_folder):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_name = root.find("filename").text
    image_path = os.path.join(image_folder, image_name)

    img_width = int(root.find("size/width").text)
    img_height = int(root.find("size/height").text)

    yolo_labels = []
    for obj in root.findall("object"):
        class_name = obj.find("name").text
        bbox = obj.find("bndbox")
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        # Convert bounding box coordinates to YOLO format
        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_labels.append(f"{class_name} {x_center} {y_center} {width} {height}")

    return image_path, yolo_labels


def convert_folder_xml_to_yolo(xml_folder, image_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith(".xml")]
    for xml_file in xml_files:
        xml_path = os.path.join(xml_folder, xml_file)
        image_path, labels = xml_to_yolo(xml_path, image_folder)

        # Save YOLO format annotation
        txt_file = os.path.splitext(xml_file)[0] + ".txt"
        output_path = os.path.join(output_folder, txt_file)
        with open(output_path, "w") as f:
            f.write("\n".join(labels))

        print(f"Converted {xml_file} to YOLO format ({txt_file})")


# Example usage
dataset = "pothole"
xml_folder = f"./{dataset}/annotations/xml/"
image_folder = f"./{dataset}/images/"
output_folder = f"./{dataset}/annotations/yolo/"
convert_folder_xml_to_yolo(xml_folder, image_folder, output_folder)
