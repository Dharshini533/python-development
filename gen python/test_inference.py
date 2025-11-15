import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# ------------------------------
# Load TFLite model
# ------------------------------
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# ------------------------------
# Load class names
# ------------------------------
with open("classes.txt", "r") as f:
    classes = [line.strip().lower() for line in f.readlines()]
print("Classes in model:", classes)

# ------------------------------
# Test folder path
# ------------------------------
test_dir = "C:/Users/Ramesh Dharshini/OneDrive/Desktop/ewasteproject/ewastetraining/testimages"

# ------------------------------
# Collect all images
# ------------------------------
test_images = []
true_labels = []
for label in os.listdir(test_dir):
    label_folder = os.path.join(test_dir, label)
    if os.path.isdir(label_folder):
        for fname in os.listdir(label_folder):
            if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                test_images.append(os.path.join(label_folder, fname))
                true_labels.append(label.lower().strip())

print("Test labels found:", set(true_labels))

# ------------------------------
# Predict and debug
# ------------------------------
correct = 0
for img_path, true_label in zip(test_images, true_labels):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    # The preprocessing step is removed because the TFLite model handles it internally.
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_details[0]['index'])[0]

    # Show probabilities
    prob_dict = {cls: float(pred[i]) for i, cls in enumerate(classes)}
    pred_class = classes[np.argmax(pred)]

    print(f"\nImage: {os.path.basename(img_path)}")
    print(f"True label: {true_label}")
    print(f"Predicted class: {pred_class}")
    print("Class probabilities:", prob_dict)

    if pred_class == true_label:
        correct += 1

# ------------------------------
# Accuracy
# ------------------------------
accuracy = (correct / len(test_images)) * 100
print(f"\nTest Accuracy: {accuracy:.2f}%")