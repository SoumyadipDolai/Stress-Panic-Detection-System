
# Stress & Panic Detection System using Voice Analysis 🎤🧠
A basic academic AI project that detects emotional stress levels using voice signals.

## Features
- Voice emotion detection
- Feature extraction using MFCC, pitch, and energy
- Support Vector Machine (SVM) model
- Web interface for recording voice
- Real-time prediction via Flask API

## Tech Stack
Python, Flask, Scikit-learn, Librosa, HTML, CSS, JavaScript

## Emotion Classes
- Calm
- Stressed
- Panic

## Project Structure
- `backend/` Flask API and model training
- `frontend/` static web UI
- `dataset_sample/` training audio organized by class
- `model/` saved trained model (`svm_model.pkl`)

## Setup and Run
1. Install dependencies:
   `pip install -r requirements.txt`
2. Ensure dataset folders exist:
   - `dataset_sample/calm`
   - `dataset_sample/stressed`
   - `dataset_sample/panic`
3. Ensure model output folder exists:
   `mkdir -p model`
4. Train model:
   `python backend/train_model.py`
5. Start backend:
   `python backend/app.py`
6. Open `frontend/index.html` in a browser and test recording.

## Verify `/predict` API
With backend running, test using:
`curl -X POST -F "file=@dataset_sample/calm/calm_01.wav" http://127.0.0.1:5000/predict`

Expected response format:
`{"emotion":"Calm 🙂"}`

## Notes
- The training script expects the dataset under `dataset_sample/` and saves the model to `model/svm_model.pkl`.
- If `model/` is missing, create it before training.
