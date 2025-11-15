import cv2
import numpy as np
import tensorflow as tf

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
print("Loaded classes:", classes)

# ------------------------------
# Initialize webcam
# ------------------------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# ------------------------------
# Eco-point counter
# ------------------------------
eco_points = 0
last_pred = None

print("\nStarting live detection... Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize for model
    img = cv2.resize(frame, (224, 224))
    img_array = np.expand_dims(img, axis=0).astype(np.float32)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]

    # Get prediction result
    pred_idx = np.argmax(predictions)
    pred_class = classes[pred_idx]
    confidence = float(predictions[pred_idx]) * 100

    # If same class predicted again, add eco-points
    if last_pred != pred_class:
        eco_points += 5
        last_pred = pred_class

    # Display results
    text = f"{pred_class.upper()} ({confidence:.1f}%) | Eco Points: {eco_points}"
    cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("E-Waste Live Detection", frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ------------------------------
# Cleanup
# ------------------------------
cap.release()
cv2.destroyAllWindows()
print("\nDetection stopped.")
print(f"Total Eco Points Earned: {eco_points}")
