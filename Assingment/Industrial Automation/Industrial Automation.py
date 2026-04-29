import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def create_data():
    data = {
        "temperature": [30,80,45,90,60,100,55,70,85,40],
        "pressure": [20,70,30,85,50,95,45,60,80,25],
        "vibration": [10,60,20,70,40,80,35,50,75,15],
        "status": [0,1,0,1,0,1,0,1,1,0]
    }
    return pd.DataFrame(data)

def train(df):
    X = df[["temperature", "pressure", "vibration"]]
    y = df["status"]
    model = DecisionTreeClassifier()
    model.fit(X, y)
    pred = model.predict(X)
    acc = accuracy_score(y, pred)
    return model, acc

def predict(model):
    temp = int(input("Temperature: "))
    pressure = int(input("Pressure: "))
    vibration = int(input("Vibration: "))
    result = model.predict([[temp, pressure, vibration]])
    if result[0] == 1:
        print("Output: Machine Failure Likely")
    else:
        print("Output: Machine Operating Normally")

df = create_data()
model, acc = train(df)

while True:
    print("\n--- Industrial System ---")
    print("1. Check Machine")
    print("2. Show Accuracy")
    print("3. Exit")
    
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        predict(model)
    elif ch == 2:
        print("Model Accuracy:", acc)
    elif ch == 3:
        break
    else:
        print("Invalid choice")
