
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



import pandas as pd

df2 = pd.read_csv('students.csv')
df2 ['name'] = df2 ['name'].str.strip()
print(df2)
df2['marks'] = df2 ['marks'].str.replace ('#',' ')
print(df2)
df2['city'] = df2 ['city'].str.replace ('*',' ')
print(df2)
df2.to_csv('clean output.csv', index = False)

df2=pd.read_csv('student.csv')
df2['name']=df2['name'].str.strip()
df2['marks']=df2['marks'].str.replace('#',' ')
df2['city']=df2['city'].str.replace('#',' ')
print(df2)