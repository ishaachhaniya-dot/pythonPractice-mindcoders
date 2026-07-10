
# x = input("Enter the plant name: ")

# if x == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif x == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", x + "!")



# A = 2000
# B = 100
# C = int(A) + int(B)
# print("sum",C)


# A = 3000
# B = 1000
# C = int(A) - int(B)
# print("substraction :",C)

# A = 200
# B = 100
# C = int(A) * int(B)
# print("multiplication :",C)

# A = 200
# B = 10
# C = int(A) / int(B)
# print("float division:",C)

# A = 7
# B = 3
# C = int(A) // int(B)
# print("floored division:",C)


# A = 7
# B = 3
# C = int(A) % int(B)
# print("modulus division:",C)


# A = 2
# B = 5
# C = int(A) ** int(B)
# print("A to the power of B :",C)


# Name = "isha achhaniya"
# Age =" 21 "
# Course = "python with aiml"
# print("Name of the student:",Name)
# print("Age of the student:",Age)
# print("Course of the student:",Course)

# Name = "isha achhaniya"
# Age =" 21 "
# Course = "python with aiml"
# print("Name of the student:",Name)
# print("Age of the student:",Age)
# print("Course of the student:",Course)

# Name = "Harshita raghuwanshi"
# Age =" 21 "
# Course = "python with aiml"
# print("Name of the student:",Name)
# print("Age of the student:",Age)
# print("Course of the student:",Course)

# Name = "Himani lahori"
# Age =" 20 "
# Course = "python with aiml"
# print("Name of the student:",Name)
# print("Age of the student:",Age)
# print("Course of the student:",Course)

# a = int(20)
# b = int(30)
# a+b
# print("sum:",a+b)

# a = 20.5
# b = 20.5
# c= float(a)*(b)
# print("float multiplication of a and b is :",c)

# char = input("enter your character:")
# print("ASCII value for your character",char,"is:",ord(char),".")

# print("*"*6)
# print(("*"+" "*4+"*\n")*4,end="")
# print("*"*6)

# for temp in range(1,7):
#     print(str(temp)*temp)

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizbuzz",end=",")
#     elif i%3==0:
#         print("fiz",end=",")
#     elif i%5==0:
#         print("buzz",end=",")
#     else:
#         print(i,end=",")


# for i in range(1,6):
#     print(i,"missisipi")
# print("ready or not,here i come")

# with open("data.txt","r") as file:
#     data=file.read()
# print(data)

# with open("student.txt","w")as f:
#     f.write('ishika,21,indore\n')
#     f.write('disha,21,indore\n')
#     f.write('bhoomika,22,indore\n')

# with open("student.txt","r")as f:
#     data=f.read()
# print(data)

# with open("student.txt","r")as f:
#     for line in f:
#         name,age,city=line.strip().split(',')
#         print(f'{name:<15}|{age:>5}|{city}')
#         print("________________")

'''Create a dataset: 
12 months of sales data for 3 products (Phones, Laptops, Tablets).
Calculate for each product: 
mean, median, std deviation, min, max, IQR
Find correlations between the 3 products' sales.
Identify any outlier months using the 3-sigma rule.
Create: 
histogram, box plot, correlation heatmap, monthly trend line chart'''

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


# # Create Dataset

# months = [
#     "Jan", "Feb", "Mar", "Apr", "May", "Jun",
#     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
# ]

# sales = pd.DataFrame({
#     "Month": months,
#     "Phones":  [120, 135, 128, 140, 150, 160, 170, 165, 155, 145, 138, 130],
#     "Laptops": [80, 85, 82, 88, 92, 96, 105, 102, 98, 90, 87, 84],
#     "Tablets": [60, 65, 63, 68, 70, 72, 78, 75, 73, 69, 66, 64]
# })

# print("Sales Dataset\n")
# print(sales)


# #  Statistics

# print(" Statistics")

# products = ["Phones", "Laptops", "Tablets"]

# for product in products:
#     data = sales[product]

#     mean = data.mean()
#     median = data.median()
#     std = data.std()
#     minimum = data.min()
#     maximum = data.max()

#     q1 = data.quantile(0.25)
#     q3 = data.quantile(0.75)
#     iqr = q3 - q1

#     print(f"\n{product}")
#     print(f"Mean      : {mean:.2f}")
#     print(f"Median    : {median}")
#     print(f"Std Dev   : {std:.2f}")
#     print(f"Minimum   : {minimum}")
#     print(f"Maximum   : {maximum}")
#     print(f"IQR        : {iqr:.2f}")


# # Correlation

# print("Correlation Matrix")

# corr = sales[products].corr()
# print(corr)


# # 3-Sigma Rule Outlier Detection

# print("Outliers (3-Sigma Rule)")

# for product in products:

#     mean = sales[product].mean()
#     std = sales[product].std()

#     lower = mean - 3 * std
#     upper = mean + 3 * std

#     outliers = sales[
#         (sales[product] < lower) |
#         (sales[product] > upper)
#     ]

#     print(f"\n{product}")

#     if outliers.empty:
#         print("No Outliers")
#     else:
#         print(outliers[["Month", product]])

# # Histogram

# plt.figure(figsize=(8,5))

# plt.hist(sales["Phones"], bins=6, alpha=0.6, label="Phones")
# plt.hist(sales["Laptops"], bins=6, alpha=0.6, label="Laptops")
# plt.hist(sales["Tablets"], bins=6, alpha=0.6, label="Tablets")

# plt.title("Sales Distribution")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()


# # Box Plot

# plt.figure(figsize=(6,5))

# plt.boxplot(
#     [sales["Phones"], sales["Laptops"], sales["Tablets"]],
#     labels=["Phones", "Laptops", "Tablets"]
# )

# plt.title("Box Plot of Sales")
# plt.ylabel("Sales")
# plt.show()


# # Correlation Heatmap

# plt.figure(figsize=(6,5))

# sns.heatmap(
#     corr,
#     annot=True,
#     cmap="coolwarm",
#     linewidths=0.5
# )

# plt.title("Correlation Heatmap")
# plt.show()


# # Monthly Trend Line Chart

# plt.figure(figsize=(10,5))

# plt.plot(months, sales["Phones"], marker="o", label="Phones")
# plt.plot(months, sales["Laptops"], marker="o", label="Laptops")
# plt.plot(months, sales["Tablets"], marker="o", label="Tablets")

# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.legend()
# plt.grid(True)
# plt.show()

'''Print the first 100 natural numbers using a for loop'''
# for num in range(1,101):
#     print(num)
 
