print("DHIVYA A 24BAD020")
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("E:\\24ADI003_24BAD020\\data.csv.zip", encoding="ISO-8859-1")
print(df.head())
print(df.info())
print(df.isnull().sum())
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
top = df.groupby("Description")["TotalSales"].sum().head(10)
top.plot(kind="bar")
plt.show()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df.groupby(df["InvoiceDate"].dt.date)["TotalSales"].sum().plot()
plt.show()
