
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

### Directory Layout
- `backend/app.py` API server with `/predict` endpoint
- `backend/train_model.py` SVM training pipeline
- `backend/utils/feature_extraction.py` audio feature extraction (MFCC, pitch, energy)
- `frontend/index.html` main UI page
- `frontend/css/style.css` UI styling
- `frontend/js/script.js` voice recording + API call logic
- `dataset_sample/calm|stressed|panic/*.wav` class-wise sample audio data
- `model/svm_model.pkl` trained model artifact

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

## Recent Changes
- Added synthetic sample audio in `dataset_sample/` to make training runnable out of the box.
- Trained and generated model artifact at `model/svm_model.pkl`.
- Improved `backend/app.py` reliability:
  - Stable model loading using absolute path resolution
  - Input validation for missing/empty uploaded file
  - Safe temporary file handling with cleanup
  - Structured error responses (`400` for bad request, `500` for processing failure)
- Verified endpoint behavior after merge:
  - Valid audio upload returns `200` with emotion
  - Missing file request returns `400` with validation error

## Final Release Note
The project is now in a stable, runnable state on `main` with:
- documented setup and verification steps
- trained model artifact and sample dataset structure
- validated backend `/predict` behavior for both success and error cases
