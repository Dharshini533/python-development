import cv2
import numpy as np
import tensorflow as tf
import csv
import datetime
import time

# Load your trained TFLite model
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Load your labels (plastic, metal, ewaste)
classes = [line.strip().lower() for line in open("classes.txt")]

# Points mapping for materials
POINTS = {
    "metal": 10,
    "plastic": 5,
    "ewaste": 15
}

# CSV filenames
CUSTOMER_CSV = "reward.csv"
SHOP_CSV = "points.csv"

def save_points_csv(filename, customer_name, material, points):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, customer_name, material, points])

def predict_label(frame):
    img = cv2.resize(frame, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], img)
    interpreter.invoke()
    predictions = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])[0]
    pred_idx = np.argmax(predictions)
    pred_label = classes[pred_idx]
    confidence = float(predictions[pred_idx])
    return pred_label, confidence

def corrected_label(frame, predicted_label):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    contrast = np.std(gray)
    mean_color = np.mean(frame, axis=(0, 1))
    blue, green, red = mean_color

    if contrast > 45 and brightness > 120:
        return "metal"
    elif (red > 80 or blue > 80 or green > 80) and brightness > 90:
        return "plastic"
    elif brightness < 80:
        return "ewaste"
    else:
        return predicted_label

# Ask for customer name
customer_name = input("Enter customer name: ")

cap = cv2.VideoCapture(0)
item_detected = False
detection_start_time = None
DETECTION_DURATION = 3  # seconds to analyze

while True:
    ret, frame = cap.read()
    if not ret:
        break

    material = ""
    seconds_left = DETECTION_DURATION

    if not item_detected:
        predicted_label, conf = predict_label(frame)
        material = corrected_label(frame, predicted_label)

        if conf > 0.4:
            if detection_start_time is None:
                detection_start_time = time.time()
            elapsed = time.time() - detection_start_time
            seconds_left = max(0, int(DETECTION_DURATION - elapsed))
            
            if elapsed >= DETECTION_DURATION:
                # Lock detection
                item_detected = True
                points = POINTS.get(material, 0)
                print(f"Item detected: {material.upper()} | Points: {points}")
                save_points_csv(CUSTOMER_CSV, customer_name, material, points)
                save_points_csv(SHOP_CSV, customer_name, material, points)
        else:
            detection_start_time = None
            seconds_left = DETECTION_DURATION

    # Display text
    display_text = f"{material.upper() if item_detected else 'Scanning...'}"
    if not item_detected:
        display_text += f" | Detecting in: {seconds_left}s"
    elif item_detected:
        display_text += f" | Points: {points}"

    color = (0, 255, 0)
    if item_detected and material == "metal":
        color = (0, 255, 255)
    elif item_detected and material == "plastic":
        color = (255, 0, 0)
    elif item_detected and material == "ewaste":
        color = (0, 0, 255)

    cv2.putText(frame, display_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    cv2.imshow("E-Waste Material Detector", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n') and item_detected:
        # Reset for next item
        item_detected = False
        detection_start_time = None
        material = ""
        print("Ready for next item...")

cap.release()
cv2.destroyAllWindows()
