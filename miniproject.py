import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("students.csv")
    print("CSV Loaded Successfully")
except FileNotFoundError:
    print("File Not Found")
    exit()

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
    'History',
    'study_hours'
]
df['total']=df[subjects].sum(axis=1)
print([['name','total']])

#calculare average
#number of subjects

df['Average'] = df[subjects].mean(axis=1)

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

#calculate ranks
df['Rank'] = df['total'].rank(ascending=False).astype(int)
print(df[['Name','Rank']])

#calculate class average
class_average = (df['Average'].mean())
print("Class Average:",round(class_average,2))

#topper of the class
Topper = df.loc[df['total'].idxmax()]#idxmax give us max value,#.loc gives full row
print("TOPPER:",Topper['Name'])

#failure rate
failed = len(df[df["Grade"]=="F"])

total_students = len(df)

failure_rate = (failed/total_students)*100

print("Failure Rate :",failure_rate)

#city wise
city_wise = df.groupby('City')['Average'].mean().astype(int)
print("City Wise Average:",city_wise)

#Bar graph on basis of city avg
plt.figure(figsize=(8,5))
city_wise.plot(kind='bar')
plt.title("City Wise Average Marks"); plt.ylabel("Average Marks"); plt.tight_layout(); plt.show()

#pie chart on basis of grade distribution
df["Grade"].value_counts().plot(
    kind="pie",autopct='%1.0f%%')
plt.title("Grade Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

#scatter plot
plt.figure(figsize=(8,5))

plt.scatter(df['study_hours'],df['Average'], s=100,alpha=0.8)
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Marks")
plt.show()

#correaltion
plt.figure(figsize=(8,6))

sns.heatmap(df[subjects].corr(),annot=True)
plt.title("Subject Correlation Heatmap")
plt.show()


report = pd.DataFrame({
    "Summary": [
        "Class Average",
        "Topper",
        "Failure Rate"
    ],
    "Value": [
        class_average,
        Topper["Name"],
        str(failure_rate) + "%"
    ]
})

report.to_csv(
    "report.csv",
    index=False
)

print("\nFiles Saved:")
print("student.csv")