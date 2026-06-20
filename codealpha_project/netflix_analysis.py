import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv("datasets/netflix_titles.csv")

# Release year count
release_count = df['release_year'].value_counts().sort_index()

# Graph
plt.figure(figsize=(12,6))
plt.plot(release_count.index, release_count.values)

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)

plt.show()