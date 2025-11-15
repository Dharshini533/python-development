# training_corrected.py
import tensorflow as tf
from tensorflow.keras import layers, models
import os

# ------------------------------
# Dataset path
# ------------------------------
data_dir = "C:/Users/Ramesh Dharshini/OneDrive/Desktop/ewasteproject/ewastedataset"
img_size = 224
batch_size = 16

# ------------------------------
# Load dataset
# ------------------------------
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_size, img_size),
    batch_size=batch_size
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_size, img_size),
    batch_size=batch_size
)

# Save lowercase class names
class_names = [c.lower() for c in train_ds.class_names]
print("Classes:", class_names)
with open("classes.txt", "w") as f:
    for c in class_names:
        f.write(c + "\n")

# ------------------------------
# Data augmentation
# ------------------------------
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
])

train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y))
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# ------------------------------
# MobileNetV2 transfer learning
# ------------------------------
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(img_size, img_size, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # phase 1

inputs = tf.keras.Input(shape=(img_size, img_size, 3))
x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
x = base_model(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.2)(x)
outputs = layers.Dense(len(class_names), activation='softmax')(x)
model = models.Model(inputs, outputs)

model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# ------------------------------
# Phase 1: Train only top layers
# ------------------------------
history1 = model.fit(train_ds, validation_data=val_ds, epochs=5)

# ------------------------------
# Phase 2: Fine-tune some base layers
# ------------------------------
base_model.trainable = True
for layer in base_model.layers[:-50]:  # freeze early layers
    layer.trainable = False

model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history2 = model.fit(train_ds, validation_data=val_ds, epochs=5)

# ------------------------------
# Save models
# ------------------------------
model.save("model.h5")
print("Saved model.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("model.tflite", "wb").write(tflite_model)
print("Saved model.tflite")
