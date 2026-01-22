print("DHIVYA A 24BAD020")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("E:\\24ADI003_24BAD020\\Housing.csv")

print(df.isnull().sum())

plt.scatter(df["area"], df["price"])
plt.show()

sns.heatmap(df.select_dtypes("number").corr(), annot=True)
plt.show()
