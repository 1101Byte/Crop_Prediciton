import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
@flask_app.route("/predict", methods=["POST"])
def predict():
    prediction_text = ""
    if request.form:  # agar form me data hai
        try:
            float_features = [float(x) for x in request.form.values()]
            features = [np.array(float_features)]
            prediction = model.predict(features)[0]  # single value
            prediction_text = f"The Predicted Crop is {prediction}"
        except:
            prediction_text = "Please enter valid input data."
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    flask_app.run(debug=True)