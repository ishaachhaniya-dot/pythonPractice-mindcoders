'''project 1'''

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# try:
#     df = pd.read_csv("students.csv")
#     print("CSV Loaded Successfully")
# except FileNotFoundError:
#     print("File Not Found")
#     exit()

# # Remove extra spaces from column names
# df.columns = df.columns.str.strip()
# #check missing values
# print(df.isnull().sum())
# #fill missing values
# df.fillna(0, inplace=True)

# #calculate total marks
# subjects = [
#     'Math',
#     'Science',
#     'English',
#     'Computer',
#     'History'
# ]
# df['total']=df[subjects].sum(axis=1)
# print(df[['name','total']])

# #calculare average
# #number of subjects

# df['Average'] = df[subjects].mean(axis=1)

# #calculate grade
# def get_grade(x):
#     if x>=90:
#         return'A+'
#     elif x>=80:
#         return 'A'
#     elif x>=70:
#         return 'B'
#     elif x>=60:
#         return 'C'
#     else:
#         return 'F'
# #calculating grade
# df['Grade'] = df['Average'].apply(get_grade)
# print(df[['Name', 'Grade']])

# #calculate ranks
# df['Rank'] = df['total'].rank(ascending=False).astype(int)
# print(df[['Name','Rank']])

# #calculate class average
# class_average = (df['Average'].mean())
# print("Class Average:",round(class_average,2))

# #topper of the class
# Topper = df.loc[df['total'].idxmax()]#idxmax give us max value,#.loc gives full row
# print("TOPPER:",Topper['Name'])

# #failure rate
# failed = len(df[df["Grade"]=="F"])

# total_students = len(df)

# failure_rate = (failed/total_students)*100

# print("Failure Rate :",failure_rate)

# #city wise
# city_wise = df.groupby('City')['Average'].mean().astype(int)
# print("City Wise Average:",city_wise)

# #Bar graph on basis of city avg
# plt.figure(figsize=(8,5))
# city_wise.plot(kind='bar')
# plt.title("City Wise Average Marks"); plt.ylabel("Average Marks"); plt.tight_layout(); plt.show()

# #pie chart on basis of grade distribution
# df["Grade"].value_counts().plot(
#     kind="pie",autopct='%1.0f%%')
# plt.title("Grade Distribution")
# plt.ylabel("")
# plt.tight_layout()
# plt.show()

# #scatter plot
# plt.figure(figsize=(8,5))

# plt.scatter(df['study_hours'],df['Average'], s=100,alpha=0.8)
# plt.xlabel("Study Hours")
# plt.ylabel("Average Marks")
# plt.title("Study Hours vs Marks")
# plt.show()

# #correaltion
# plt.figure(figsize=(8,6))

# sns.heatmap(df[subjects].corr(),annot=True)
# plt.title("Subject Correlation Heatmap")
# plt.show()


# report = pd.DataFrame({
#     "Summary": [
#         "Class Average",
#         "Topper",
#         "Failure Rate"
#     ],
#     "Value": [
#         class_average,
#         Topper["Name"],
#         str(failure_rate) + "%"
#     ]
# })

# report.to_csv(
#     "report.csv",
#     index=False
# )

# print("\nFiles Saved:")
# print("student.csv")


'''project 2'''

# items={
#     'single size bedsheet':160,
#     'double size bedsheet':250,
#     'pillow covers':50,
#     'comforter':240,
#     '3*4 bedsheet':200
# }
# print("welcome to YASH HANDLOOMS")
# print("here's our menu:")
# print("single size bedsheet:160 rs\ndouble size bedsheet:250 rs\npillow covers:50 rs\ncomforter:240 rs\n3*4 bedsheet:200 rs")

# total_order=0

# item_1=input("Enter the name of item you want to order=")
# if item_1 in items:
#     total_order+=items[item_1]
#     print(f'{item_1} added to bill')
# else:
#     print(f'orderd item {item_1} not available yet!')
# another_order=input("do you want to add another item?(yes/no)")
# if another_order=="yes":
#     item_2=input("enter second item=")
#     if item_2 in items:
#         total_order+=items[item_2]
#         print(f'{item_2} has been added')
#     else:
#         print(f'orderd item {item_2} not available yet!')
# more_to_add=input("do you want to add third item?(yes/no)")
# if more_to_add=="yes":
#     item_3=input("enter third item=")
#     if item_3 in items:
#         total_order+=items[item_3]
#         print(f'{item_3}added')
#     else:
#         print(f'{item_3}not available yet!')
# print(f'The total amount of items to pay --> {total_order}')


'''project 3'''

# height=float(input("Enter your height in cm:"))
# weight=float(input("Enter weight in kg:"))
# height=height/100
# BMI=weight/(height*height)
# print("your body mass index is:")
# if(BMI>0):
# 	if(BMI<=16):
# 		print("you are critically underweight")
# 	elif(BMI<=18):
# 		print("underweight")
# 	elif(BMI<=25):
# 		print("you are Healthy")
# 	elif(BMI<=30):
# 		print("you are overweight")
# 	else: print("you are critically overweight")
# else:("enter valid details")

'''project 4'''

import random
# cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
# ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

# def picking_card():
#     card = random.choices(cards)
#     rank = random.choices(ranks)
#     return(f"The {rank} of {card}")

# print(picking_card()

''' project 4'''
