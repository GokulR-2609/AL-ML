# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Use one feature for easy visualization
X = data[['income']]   # independent variable
y = data['target']     # dependent variable

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# Scatter plot (actual data)
plt.scatter(X_test, y_test)

# Plot regression line
plt.plot(X_test, y_pred)

# Labels
plt.xlabel("Income")
plt.ylabel("Target")
plt.title("Linear Regression - Prediction")

# Show plot
plt.show()