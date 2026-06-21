import pandas as pd
import matplotlib.pyplot as plt
import os

# Dataset load
df = pd.read_csv("datasets/netflix_titles.csv")

# Images folder create agar na ho
os.makedirs("images", exist_ok=True)

# -------------------------------
# Graph 1: Movies vs TV Shows
# -------------------------------
type_count = df['type'].value_counts()

plt.figure(figsize=(6,4))
type_count.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/Figure_1.png")
plt.show()

# -------------------------------
# Graph 2: Content Distribution
# -------------------------------
plt.figure(figsize=(6,6))
type_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Content Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/Figure_2.png")
plt.show()

# -------------------------------
# Graph 3: Releases Over Years
# -------------------------------
release_count = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(release_count.index, release_count.values)
plt.title("Netflix Releases Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/Figure_3.png")
plt.show()

# -------------------------------
# Graph 4: Top 10 Countries
# -------------------------------
country_count = (
    df['country']
    .dropna()
    .str.split(', ')
    .explode()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,5))
country_count.plot(kind='bar')
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/Figure_4.png")
plt.show()

# -------------------------------
# Graph 5: Content Added Per Year
# -------------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
added_year = df['date_added'].dt.year.value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(added_year.index, added_year.values, marker='o')
plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/Figure_5.png")
plt.show()

print("All graphs saved successfully in images folder!")