from PIL import Image
import os

# Path to your testimages folder
folder_path = "testimages"  # change if needed

# Target format
target_format = "jpg"

# Loop through all class folders
for class_folder in os.listdir(folder_path):
    class_path = os.path.join(folder_path, class_folder)
    if os.path.isdir(class_path):
        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            
            # Open image
            try:
                with Image.open(img_path) as img:
                    # Convert to RGB (important for PNG/WebP with alpha channel)
                    img = img.convert("RGB")
                    # New filename with jpg extension
                    new_name = os.path.splitext(img_name)[0] + "." + target_format
                    new_path = os.path.join(class_path, new_name)
                    img.save(new_path, target_format.upper())
                    # Optional: remove old file if different
                    if new_path != img_path:
                        os.remove(img_path)
            except Exception as e:
                print(f"Error converting {img_path}: {e}")

print("All images converted to", target_format)
