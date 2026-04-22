
import os
import numpy as np
import joblib
from sklearn import svm
from sklearn.model_selection import train_test_split
from utils.feature_extraction import extract_features

dataset_path = "../dataset_sample"

labels = {"calm":0,"stressed":1,"panic":2}

X=[]
y=[]

for label in labels:

    folder = os.path.join(dataset_path,label)

    if not os.path.exists(folder):
        continue

    for file in os.listdir(folder):

        path = os.path.join(folder,file)

        try:
            features = extract_features(path)
            X.append(features)
            y.append(labels[label])
        except:
            pass

X = np.array(X)
y = np.array(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = svm.SVC(kernel="linear")
model.fit(X_train,y_train)

acc = model.score(X_test,y_test)
print("Model Accuracy:",acc)

joblib.dump(model,"../model/svm_model.pkl")
