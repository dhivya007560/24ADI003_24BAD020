print("DHIVYA A 24BAD020")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:\\24ADI003_24BAD020\\diabetes.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols] = df[cols].replace(0, pd.NA)

print(df.isnull().sum())

plt.hist(df["Glucose"].dropna(), bins=20)
plt.show()

plt.boxplot(df["Age"])
plt.show()
