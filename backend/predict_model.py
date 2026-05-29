import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load dataset
diabetes_dataset = pd.read_csv('diabetes.csv')

# Split features and labels
X = diabetes_dataset.drop('Outcome', axis=1)
Y = diabetes_dataset['Outcome']

# Standardize
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

X = standardized_data
Y = diabetes_dataset['Outcome']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train SVM
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Accuracy check (optional)
train_acc = accuracy_score(classifier.predict(X_train), Y_train)
test_acc = accuracy_score(classifier.predict(X_test), Y_test)
print(f"✅ Model trained. Train Acc: {train_acc:.2f}, Test Acc: {test_acc:.2f}")

# Function for prediction
def predict_diabetes(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"
