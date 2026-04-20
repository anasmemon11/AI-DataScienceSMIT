from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

model = load_model("face_model.h5")

labels = ["ahmed","ali","basit"]

def predict_image(img_path):

    img = Image.open(img_path)
    img = img.resize((128,128))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    return labels[np.argmax(prediction)]

@app.route("/", methods=["GET","POST"])

def index():

    label = None

    if request.method == "POST":

        file = request.files["image"]
        path = "static/upload.jpg"
        file.save(path)

        label = predict_image(path)

    return render_template("index.html", label=label)

if __name__ == "__main__":
    app.run(debug=True)
