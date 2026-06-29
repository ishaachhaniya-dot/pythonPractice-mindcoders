
# age = 4
# print(age)

# name ="Isha"
# profession="Software learner"
# experience = 1
# print("Hello, I am",name,".I am",profession,".I have",experience,"year experience.")

# x = 5
# print(type(x))
# x ="5"
# print(type(x))
# x = 5.5
# print(type(x))
# x = 1j
# print(type(x))
# x = True
# print(type(x))
# x =["apple","banana","cherry"]
# print(type(x))
# x =("apple","banana","cherry")
# print(type(x))
# x ={"apple","banana","cherry"}
# print(type(x))
# x =range(6)
# print(type(x))
# x =True
# print(type(x))
# x =frozenset({"apple","banana","cherry"})
# print(type(x))
# x =b"Hello"
# print(type(x))
# x =bytearray((5))
# print(type(x))
# x = None
# print(type(x))
# x = memoryview(bytes(5))
# print(type(x))
# x ={"a":"1","b":"2"}
# print(type(x))



# print(5 >> 2)

# x = 1
# print(x:=3)

# x = 4
# print(x<5 and x<10)
# print(x>5 or x>10)
# print(not(x<5 or x<10))



# x = 10
# y = 20
# print(x is y)


# x = 10 
# y = "10"
# print(x is y)


# x = ["MARUTI" , "BMW"]
# Y = "MARUTI1"

# print(y in x)

  
#x = int(input("Enter first side of triangle:"))
#y = int(input("Enter second side of triangle:"))
#z = (x ** 2 + y ** 2)**0.5
#print(z)


# print("+----------+")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("+----------+")


# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5, end="")
# print("+"+"-"*10+"+")


# number1 = int(input("Enter the first number:"))
# number2= int(input("Enter the second number:"))
# if number1 > number2:
#     larger_number = number1
# else :
#     larger_number = number2
# print("The larger number is:",larger_number) 


# number1 = int(input("Enter the first number:"))
# number2= int(input("Enter the second number:"))
# number3= int(input("Enter the third number:"))

# largest_number = number1

# if number2 > largest_number:
#     larger_number = number2
# if number3 > largest_number:
#     larger_number = number3

#     print("The larger number is:",larger_number) 

# number1 = int(input("Enter the first number:"))
# number2= int(input("Enter the second number:"))
# number3= int(input("Enter the third number:"))

# largest_number = max(number1,number2,number3)
# lowest_number = min(number1,number2,number3)

# print("The largest number is:", largest_number)
# print("The lowest number is:", lowest_number)


# x = input("Enter the plant name:")

# if x == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif x == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else :
#     print("Spathiphyllum! Not", x +"!")

# while True:
#     print ("I am not able to end this.")


# largest_number = -99999999
# number = int(input("Enter a number or type -1 to stop:"))
# while number !=-1:
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to stop:"))

# print("The largest number is:",largest_number)

# number = int(input("Enter the number:"))
# count=1
# while count<=number:
#     print(count," ",end="",)
#     count+=1


# number = int(input("Enter the number:"))
# count=1
# even =0
# odd =0
# while count<=number:
#    if count % 2 == 0:
#         even += 1
#    else:
#        odd +=1
#    count += 1
   
# print("Even=", even)
# print("odd=", odd)


# for counter in range(101):
#     print("counter:",counter)
#     pass

# for counter in range (1,10):
#     print("The value :",counter)

# for counter in range (1,10,2):
#     print("The value :",counter)


# for counter in range (1,1):
#     print("The value :",counter)


# for counter in range (2,1):
#     print("The value :",counter)


# power=1
# for expo in range(16):
#     print("2 to the power of",expo,"is",power)
#     power *=2



# print("The break instruction:")
# for counter in range(1,6):
#     if counter == 3:
#         break
#     print("Inside the loop.", counter)
# print("outside the loop. ")


# print("The break instruction:")
# for counter in range(1,6):
#     if counter == 3:
#         continue
#     print("Inside the loop.", counter)
# print("outside the loop. ")


# counter = 1 
# while counter < 5:
#      print(counter) 
#      counter += 1 
# else:
#     print("else:", counter)


# counter = 5
# while counter < 5:
#      print(counter) 
#      counter += 1 
# else: 
#      print("else:", counter)

# var=10
# print(var>0)
# print(not(var<=0))

# print(var!=0)
# print(not(var==0))

# i = 1
# j = not not i

# numbers = [10,5,7,2,1]
# print(numbers)
# print(type(numbers))

# why list starts from 0 in python 
# numbers[0]=> numbers address +((number of bytes occupied * index)) //answer 1st pos
# numbers[1]=> numbers address +((number of bytes occupied * index)) //answer 2nd pos
# numbers[2]=> numbers address +((number of bytes occupied * index))  // answer 3rd pos

# numbers =[]
# numbers =[2,3,4,5]
# print("list contents",numbers)

# print("first element",numbers[0])
# print("second element",numbers[1])
# print("third element",numbers[2])

# numbers[0] = 22
# print("numbers[0]",numbers[0])
# print(numbers)

# numbers[1]=numbers[3]
# print(numbers)

# print(len(numbers))
# del numbers[2]
# print(numbers)
# print(numbers[-1])
# print(numbers[-3])
# print(numbers[-4]) //out of range

# //practice question
# list =[1,2,3,4,5]
# print(len(list))
# del list[4]
# print(len(list))
# i= int(input("enter the number:"))
# list[int(len(list)//2)]=i
# # print(list)
# list =[1,2,3,4,5]
# print(list)
# list.insert(0,3)    
# print(list)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])


# list= []
# for iterator in range(1,11):
#     list.append(iterator)
# print(list)

# list= []
# for iterator in range(10):
#     list.append(iterator+1)
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for count in range(10):
#     list[count]+=1
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# total =0
# for sum in list:
#     total+= sum
# print(list)
# print(total)

# auxiliary=variable_1
# variable_1=variable_2

# variable_1=1
# variable_2=2

# print("variable_1:",variable_1)
# print("variable_2:",variable_2)

# variable_1,variable_2=variable_2,variable_1

# print("variable_1:",variable_1)
# print("variable_2:",variable_2)

# list=[1,2,3,4]
# print(list)
# list[1],list[3]=list[3],list[1]
# print(list)

# n=int(input("enter number:"))
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)

rows = 5  # Number of rows in the triangle

# Outer loop: controls the number of rows
for i in range(1, rows + 1):
    for j in range(1, i + 1):  # Inner loop: controls the number of stars in each row
        print("*", end=" ")  # Print a star and a space (no newline)
    print()  # Move to the next line after each row is printed