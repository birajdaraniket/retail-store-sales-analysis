import pandas as pd

data = pd.read_csv("C:/Users/HP/Desktop/Data Analyst/retail_store_sales.csv")

df = pd.DataFrame(data)
df.info()
print(df.isnull().sum())

# changes the null values of items 
df["Item"] = df["Item"].fillna("Unknown item")
print(df.head(10))
df.info()

# changes the null values of Price per unit 
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit"].mean())
print(df.head(10))
df.info()

# changes the null values of quantity
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean()).round().astype(int)
print(df.head(10))
df.info()

# changes the null values of total spent
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")
df["Total Spent"] = df["Total Spent"].fillna(df["Price Per Unit"]* df["Quantity"]).round().astype(int)
print(df.head(10))
df.info()

# changes the null values of Discount Applied
df["Discount Applied"] = df["Discount Applied"].fillna(df["Discount Applied"].mode()[0])
print(df.head(10))
df.info()

#changes the data type of Transaction date
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce", format="mixed")
print(df.tail(10))
df.info()

# after every changes i use print(df.head(10)) or print(df.tail(10)), df.info() for checking work is done properly or not..!

print(df.shape)   # check rows & columns
print(df.head())  # quick preview
print(df.isnull().sum()) # CHECK null values again for validation 

# save cleaned file
df.to_csv("C:/Users/HP/Desktop/Data Analyst/retail_store_sales_cleaned.csv", index=False)

# Data cleaning process is done...!