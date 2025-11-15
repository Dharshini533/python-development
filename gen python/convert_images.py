import os
from PIL import Image

# Path to your dataset
dataset_dir = r"..\ewastedataset"

# Loop through all class folders
for class_folder in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_folder)
    if os.path.isdir(class_path):
        # Loop through all images in class folder
        for filename in os.listdir(class_path):
            file_path = os.path.join(class_path, filename)
            try:
                # Open the image
                with Image.open(file_path) as img:
                    # Convert to RGB (important for PNG with transparency)
                    img = img.convert("RGB")
                    # Save as JPG with same name but .jpg extension
                    new_file_path = os.path.splitext(file_path)[0] + ".jpg"
                    img.save(new_file_path, "JPEG")
                    
                # Optional: delete old file if it was not jpg
                if file_path != new_file_path:
                    os.remove(file_path)

            except Exception as e:
                print(f"Could not process {file_path}: {e}")
