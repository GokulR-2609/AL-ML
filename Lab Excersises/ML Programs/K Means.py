# Import libraries
import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("data.csv")

# Select features for clustering
X = data[['age','income']]

# Create K-Means model
kmeans = KMeans(n_clusters=3)

# Fit the model
kmeans.fit(X)

# Predict clusters
clusters = kmeans.predict(X)

# Add cluster labels to dataset
data['Cluster'] = clusters

# Display dataset with clusters
print(data)