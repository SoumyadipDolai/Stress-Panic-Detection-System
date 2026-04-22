
import librosa
import numpy as np

def extract_features(file_path):

    audio,sr = librosa.load(file_path,sr=None)

    mfcc = np.mean(librosa.feature.mfcc(y=audio,sr=sr,n_mfcc=13).T,axis=0)

    pitch = np.mean(librosa.yin(audio,fmin=50,fmax=300))

    energy = np.mean(librosa.feature.rms(y=audio))

    features = np.hstack((mfcc,pitch,energy))

    return features
