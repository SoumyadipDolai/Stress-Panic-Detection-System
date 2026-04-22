
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import tempfile
from utils.feature_extraction import extract_features

app = Flask(__name__)
CORS(app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "svm_model.pkl")
model = joblib.load(MODEL_PATH)
model = joblib.load("../model/svm_model.pkl")

labels = {
    0:"Calm 🙂",
    1:"Stressed 😟",
    2:"Panic 🚨"
}

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error":"Missing audio file. Use form-data key 'file'."}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error":"Empty filename provided."}), 400

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_path = temp_file.name
            file.save(temp_path)

        features = extract_features(temp_path)
        prediction = model.predict([features])[0]
        emotion = labels[prediction]
        return jsonify({"emotion":emotion})
    except Exception:
        return jsonify({"error":"Failed to process audio file."}), 500
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)
