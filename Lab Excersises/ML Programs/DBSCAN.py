# Import libraries
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("data.csv")

# Select features
X = data[['age', 'income']]

# Scale the data
X = StandardScaler().fit_transform(X)

# Apply DBSCAN
model = DBSCAN(eps=0.5, min_samples=3)
clusters = model.fit_predict(X)

# Show cluster labels
print("Cluster labels:")
print(clusters)

# Add clusters to dataset
data['Cluster'] = clusters
print(data)