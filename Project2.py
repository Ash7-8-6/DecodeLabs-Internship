# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt



# Reading Excel File
excel_data = pd.read_excel("Dataset for Data Analytics.xlsx")
# print(excel_data[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].describe())

# Mean, median, and count
print("\nMean:")
print(excel_data[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].mean())

print("\nMedian:")
print(excel_data[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].median())

print("\nCount:")
print(excel_data[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].count())

# Create histogram for TotalPrice for checking the skewness 
plt.figure(figsize=(8, 5))
plt.hist(excel_data["TotalPrice"], bins=20)

# Add labels and title
plt.title("Distribution of TotalPrice")
plt.xlabel("TotalPrice")
plt.ylabel("Frequency")

# Orders by year
excel_data["Date"] = pd.to_datetime(excel_data["Date"])
print("\nOrders by Year:")
print(excel_data["Date"].dt.year.value_counts().sort_index())

# Detecting Outlier(Noise) In TotalPrice
plt.boxplot(x=excel_data["TotalPrice"])
plt.show()
Q1 = excel_data["TotalPrice"].quantile(0.25)
Q3 = excel_data["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

outliers = excel_data[(excel_data["TotalPrice"]<lower_bound) |(excel_data["TotalPrice"]>upper_bound)]

print("Number of outliers:", len(outliers))
print(outliers)

