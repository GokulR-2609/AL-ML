import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def create_data():
    data = {
        "hour": [8,9,17,18,22,2,7,12,15,20],
        "day": [1,1,5,5,6,7,2,3,4,6],
        "traffic": [2,2,2,2,1,0,1,1,2,1]
    }
    return pd.DataFrame(data)

def train(df):
    X = df[["hour", "day"]]
    y = df["traffic"]
    model = RandomForestClassifier()
    model.fit(X, y)
    pred = model.predict(X)
    acc = accuracy_score(y, pred)
    return model, acc

def predict(model):
    hour = int(input("Hour (0-23): "))
    day = int(input("Day (1-7): "))
    result = model.predict([[hour, day]])
    levels = ["Low", "Medium", "High"]
    print("Output: Traffic Level =", levels[result[0]])

df = create_data()
model, acc = train(df)

while True:
    print("\n--- Smart City System ---")
    print("1. Predict Traffic")
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
