import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population_data.csv")
plt.figure()
plt.hist(df["Age"], bins=6)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution Histogram")
plt.show()
df["Gender"].value_counts().plot(kind="bar")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution Bar Chart")
plt.show()
