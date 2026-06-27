<<<<<<< HEAD
import numpy as np
=======
StudentRecords=[
    ['Name','Age','City','Math','Science','English','Computer','History'],
    ['Rahul',18,'Bhopal',78,82,75,88,80],
    ['Priya',17,'Indore',92,95,90,96,94],
    ['Amit',18,'Jabalpur',65,70,68,72,66],
    ['Neha',17,'Bhopal',88,84,86,90,87],
    ['Rohan',18,'Indore',55,60,58,62,57],
    ['Sneha',17,'Gwalior',81,79,83,85,80],
    ['Arjun',18,'Bhopal',74,76,72,78,75],
    ['Kiran',17,'Indore',90,89,91,93,88],
    ['Vikas',18,'Jabalpur',49,52,50,55,48],
    ['Anjali',17,'Gwalior',85,88,84,86,89],
    ['Pooja',18,'Bhopal',84,81,79,88,82],
    ['Manish',17,'Indore',76,72,74,78,75],
    ['Sakshi',18,'Gwalior',91,93,89,95,92],
    ['Deepak',17,'Jabalpur',62,65,60,68,64],
    ['Nisha',18,'Bhopal',87,85,88,90,86],
    ['Yash',17,'Indore',71,69,73,75,72],
    ['Kavita',18,'Gwalior',95,97,94,98,96],
    ['Mohit',17,'Jabalpur',58,55,60,62,57],
    ['Ritika',18,'Bhopal',82,84,80,86,83],
    ['Akash',17,'Indore',67,70,66,72,68],
    ['Simran',18,'Gwalior',89,87,90,91,88],
    ['Harsh',17,'Jabalpur',45,50,48,52,47],
    ['Meena',18,'Bhopal',78,80,76,82,79],
    ['Rajat',17,'Indore',93,91,94,96,92],
    ['Manya',18,'Gwalior',74,77,72,79,75]
]
>>>>>>> 5be27bc228e9305f5fa217dba8d8480c28147208
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

<<<<<<< HEAD
try:
    df = pd.read_csv("students.csv")
    print("CSV Loaded Successfully")
except FileNotFoundError:
    print("File Not Found")
    exit()

=======
df = pd.read_csv("students.csv")
print(df)
>>>>>>> 5be27bc228e9305f5fa217dba8d8480c28147208
# Remove extra spaces from column names
df.columns = df.columns.str.strip()
#check missing values
print(df.isnull().sum())
#fill missing values
print(df.fillna(0, inplace=True))

#calculate total marks
subjects = [
    'Math',
    'Science',
    'English',
    'Computer',
    'History'
]
df['total']=df[subjects].sum(axis=1)
print([['name','total']])

#calculare average
<<<<<<< HEAD
#number of subjects

df['Average'] = df[subjects].mean(axis=1)
=======
#number of subjects=5
df['average']=df['total']/5
print(df[['name','average']])
>>>>>>> 5be27bc228e9305f5fa217dba8d8480c28147208

#calculate grade
def get_grade(x):
    if x>=90:
        return'A+'
    elif x>=80:
        return 'A'
    elif x>=70:
        return 'B'
    elif x>=60:
        return 'C'
    else:
        return 'F'
#calculating grade
df['Grade'] = df['Average'].apply(get_grade)
print(df[['Name', 'Grade']])



