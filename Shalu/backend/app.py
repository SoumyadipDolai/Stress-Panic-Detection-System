
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from utils.feature_extraction import extract_features

app = Flask(__name__)
CORS(app)

model = joblib.load("../model/svm_model.pkl")

labels = {
    0:"Calm 🙂",
    1:"Stressed 😟",
    2:"Panic 🚨"
}

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]
    path = "temp.wav"
    file.save(path)

    features = extract_features(path)

    prediction = model.predict([features])[0]
    emotion = labels[prediction]

    os.remove(path)

    return jsonify({"emotion":emotion})

if __name__ == "__main__":
    app.run(debug=True)
