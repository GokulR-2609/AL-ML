import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data():
    return pd.read_csv("diabetes.csv")

def train_model(data):
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return model, acc

def predict(model):
    preg = int(input("Pregnancies: "))
    glucose = int(input("Glucose: "))
    bp = int(input("Blood Pressure: "))
    skin = int(input("Skin Thickness: "))
    insulin = int(input("Insulin: "))
    bmi = float(input("BMI: "))
    dpf = float(input("DPF: "))
    age = int(input("Age: "))
    result = model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    if result[0] == 1:
        print("Output: High risk of Diabetes")
    else:
        print("Output: Low risk of Diabetes")

data = load_data()
model, acc = train_model(data)

while True:
    print("\n--- Healthcare System ---")
    print("1. Check Patient")
    print("2. Show Accuracy")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        predict(model)
    elif choice == 2:
        print("Model Accuracy:", acc)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
