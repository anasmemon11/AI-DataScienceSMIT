import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from sklearn.metrics import classification_report

# Load Dataset
(X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()

# Normalize images
X_train = X_train / 255.0
X_test = X_test / 255.0

# CNN Model
model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=10)

# Evaluate
predictions = model.predict(X_test)
predicted_classes = predictions.argmax(axis=1)

print(classification_report(y_test, predicted_classes))
