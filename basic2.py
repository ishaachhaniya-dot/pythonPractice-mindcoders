'''list in python'''
# numbers = [10,5,7,2,1]
# print(numbers)
# print(type(numbers))

'''why list starts from 0 in python''' 
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

'''practice question'''
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

# my_list = [1,2,3,4,5,6,7,8,9]
# for count in range(len(my_list)):
# print

# n=int(input("enter number:"))
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)


# numbers=[1,2,3,4,5]
# numbers.append(6)
# print(numbers)

''' rishabh'''
# my_list = [8, 10, 6, 2, 4]
# print(my_list) 
# count = 0
# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#         count += 1
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i] 
# print(my_list)
# print(count)

''' sirr'''
# my_list=[1,2,3,4,5]
# # my_list=[8,10,6,2,4]
# swapped= True
# count=0
# index=0
# while swapped:
#     swapped= False 
#     for i in range(len(my_list)-1-index):
#          count+=1
#          if my_list[i]>my_list[i+1]:
#             swapped = True
#             my_list[i],my_list[i+1]= my_list[i+1],my_list[i]
# print(my_list)
# print(count)

'''sorting and reverse'''
# my_list = [8, 10, 6, 2, 4] 
# my_list.sort() 
# print(my_list)
# my_list.reverse()
# print(my_list)

'''slicing'''
# my_list = [10, 8, 6, 4, 2] 
# new_list = my_list[1:3]
# print(new_list)

# my_list = [10, 8, 6, 4, 2] 
# new_list = my_list[1:-1]
# print(new_list)

# my_list = [10, 8, 6, 4, 2] 
# new_list = my_list[-1:1] 
# print(new_list)

# my_list = [10, 8, 6, 4, 2] 
# new_list = my_list[:3] 
# print(new_list)

# my_list = [10, 8, 6, 4, 2] 
# new_list = my_list[3:] 
# print(new_list)

# my_list = [10, 8, 6, 4, 2] 
# del my_list[1:3] 
# print(my_list)


# my_list = [10, 8, 6, 4, 2] 
# del my_list[:] 
# print(my_list)

# row=[]
# for i in range(8):
#     row.append("WHITE_PAWN")
# print(row)

'''list comprehention'''
# row=["WHITE_PAWN" for i in range(8)]
# print(row)

# squares=[ x **2 for x in range(10)]
# print(squares)

# twos=[2** index for index in range(10)]
# print(twos)

# squares = [index ** 2 for index in range(10)]
# odds=[index for index in squares if index %2 != 0]
# print(odds) 

# even = [index for index in squares if index %2 ==0]
# print(even)

'''two dimentional array'''
# board =[]
# for i in range(8):
#     row =["EMPTY" for i in range(8)]
#     board.append(row)

# board = []
# for i in range(8):
#      row = ["EMPTY" for i in range(8)]  
#      board.append(row)

# print(board)

     
# board[0][0]="ROOK"
# board[0][7]="ROOK"
# board[7][0]="ROOK"
# board[7][7]="ROOK"

# print("------------")

# for element in board:
#     print(element)

# board[0][1]="KNIGHT"
# board[0][6]="KNIGHT"
# board[7][1]="KNIGHT"
# board[7][6]="KNIGHT"
# print("------------")
# for element in board:
#     print(element)

# temps = [[0.0 for h in range(24)] for d in range(31)]
# temp1 = 19
# temp2 = 32
# count = 0


# for days in temps:
#     if count== 0:
#         days[11]=temp1
#         count = 1
#     else:
#         days[11]= temp2
#         count=0

# for element in temps:
#     print(element)

# total=0.0
# for days in temps:
#     total+=days[11]
# average = total/31
# print("Average temperature at noon:",average)

# highest = -100.0 
# for day in temps:
#      for temp in day:
#         if temp > highest:
#             highest = temp
# print("Highest temp:",highest)


# hot_days=0
# for day in temps:
#     if day[11]>20.0:
#         hot_days +=1
# print(hot_days,"days were hot")

#--------> multidimentional array
# rooms = [[[False for r in range(20)] for f in range(15)]for t in range(3)]
# print(rooms)

# rooms[1][9][13] = True
# rooms[0][4][1]= True

# vacancy=0
# for room_number in range(20):
#     # if not rooms[2][14][room_number]:
#     if not rooms[1][9][room_number]:

#         vacancy+=1
# print("vacancy in 3rd 15th floor",vacancy)

#-------->scope
# def scope_test():
# x = 123
# scope_test()
# print(x)


# def my_function():
#     print("DO i know that varible",var)

# var =1
# my_function()
# print(var)

#-------->global variable
# def my_function():
#     global var
#     var =2
#     print("DO i know that variable",var)

# var =1
# my_function
# print(var)


# def my_function():
#     global var
#     var =5
#     return var
# print(return_var())
# print(var)

# def my_function(n):
#     print("I got",n)
#     n+=1
#     print("I have",n)

# var =1
# my_function(var)
# print(var)
#-------->tuple
# def my_function(my_list_1):
#         print("Print #1:", my_list_1)
#         print("Print #2:", my_list_2)
#         my_list_1 = [0, 1]
#         print("Print #3:", my_list_1)
#         print("Print #4:", my_list_2) 
        
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


# def my_function(my_list_1):
#         print("Print #1:", my_list_1)
#         print("Print #2:", my_list_2)
#         del my_list_1[0]
#         print("Print #3:", my_list_1)
#         print("Print #4:", my_list_2) 
        
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)
#--------->recursion
# def countdown(number):
#     print(number)

#     if number==0:
#         return
#     else:
#         print("going in rec:",number)
#         countdown(number-1)
#         print("out",number)
# print("Starting recursion")
# countdown(5)
# print(" Ending recursion")


# def factorial(number):
#     if number <=0:
#         return 1
#     else:
#         return number * factorial(number-1)
# print(factorial(5))
    
# my_tuple = (1, 10, 100)
# t1 = my_tuple + (1000, 10000) 
# t2 = my_tuple * 3 
# print(len(t2)) 
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)
    

# # my_tuple = (10,100,1000)
# # my_tuple +=(1000,10000)
# # print(my_tuple)

# tuple_1=(1,2,3)
# for elem in tuple_1:
#     print(elem)

# tuple_2=(1,2,3,4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3=(1,2,3,4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4=tuple_1+tuple_2
# tuple_5=tuple_3*2
# print(tuple_4)
# print(tuple_5)

# my_tuple =tuple((1,2,"string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list=[1,2,3]
# print(my_list)
# print(type(my_list))
# tup=tuple(my_list)
# print(tup)
# print(type(tup))

# var=123
# t1=(1,)
# t2=(2,)
# t3=(3,var)

# t1,t2,t3=t2,t3,t1
# print(t1,t2,t3)
# print(type(t1),type(t2),type(t3))
#-------->dictionary
# dictionary={
# "cat": "chat",
# "dog": "chien",
# "horse": "cheval"
# }
# phone_numbers={'boss':555, 'suzy':222}
# empty_dictionary={}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary['cat'])
# print(phone_numbers["suzy"])

# print(phone_numbers['president'])

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}# words = ['cat', 'lion', 'horse']
# # for word in words:
# #     if word in dictionary:
# #         print(word, "->", dictionary[word])
# #     else:      
# #         print(word, "is not in dictionary")

# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key,"--",dictionary[key])

# for key,value in dictionary.items():
#     print(key,"--",value)
# for value in dictionary.values():
#     print(value)


# pol_eng_dictionary = {    
#                           "zamek": "castle",
#                           "woda": "water",
#                           "gleba": "soil" 
#                                 }
# copy_dictionary = pol_eng_dictionary.copy()
# print("copy_dictionary:",copy_dictionary)

# pol_eng_dictionary["zamek"] = "lock" 
# item = pol_eng_dictionary["zamek"] 
# print(item) 

# phonebook = {}
# print(phonebook)
# phonebook["Adam"] = 3456783958 
# print(phonebook)
# del phonebook["Adam"]
# # print(phonebook)

# pol_eng_dictionary ={
#     "zameek":"castle",
#     "woda":"water",
#     "gleba":"soil",
# }
# # if "zameek" in pol_eng_dictionary:
# #     print("yes")
# # else:
# #     print("nos")

# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zameek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(len(pol_eng_dictionary))
 
 #-------->problem
# student = {}
# while True:
#         name = input("Enter student name")
#         if name=='':
#              break
#         score = int(input("enter student score"))
#         if score not in range(1,11):
#              break
#         if name in student:
#              student[name]+=(score,)
#         else:
#              student[name]=(score,)
# # for mark in student:
# #         print(mark)
# print(student)    

# for name,score in student.items():
#       sum=0
#       for s in score:
#             sum+=s
#       print(name,"->",sum/len(score))

# student={}
# while True:
#       name=input("enter name:")
#       if name=='':
#             break
#       score = int(input("enter score:"))
#       if score not in range(1,11):
#             break
#       if name in student:
#             student[name]+=(score,)
#       else:
#             student[name]=(score,)
# print(student)
# for name,score in student.items():
#         sum=0
#         for s in score:
#               print(name,"->",sum/len(score))
#-------->object oriented programming
# class ThisIsMyFirstClass:
#      name="isha"
#      age=21

#      def getName(self):
#           print(self.name)
# firstObject = ThisIsMyFirstClass()
# print(firstObject)
# firstObject.getName()

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.age=0
#         self.gender=""
#         self.grade=""

# isha = Student()
# print(isha)

# isha.name="isha achhaniya"
# isha.age=21
# isha.gender="female"
# isha.grade= "2nd yr"

# print(isha.name)
# print(isha.age)
# print(isha.gender)
# print(isha.grade)

# class Student:
#     def __init__(self,name,age,gender,grade):
#         self.grade = grade
#         self.name=name
#         self.age=age
#         self.gender=gender

#     def printDetails(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Gender:",self.gender)
#         print("Grade:",self.grade)

# isha = Student("isha achhaniya",21,"female","2nd year")
# print(isha)

# isha.printDetails()

# class ExampleClass:
#     def __init__(self,val=1):
#         self.first = val
#     def set_second(self,val):
#         self.second = val

# object_1=ExampleClass()
# object_2=ExampleClass(2)
# object_2.set_second(3)
# object_3=ExampleClass(4)
# object_3.third = 5

# print(object_1.__dict__)
# print(object_2.__dict__)
# print(object_3.__dict__)

# class classy:
#     def method(self,par):
#         print("method",par)
# obj=classy() 
# obj.method(1)       

# class classy:
#     vria=2
#     def method(self):
#         print(self.vria,self.var)
# obj=classy()
# obj.var=3
# obj.method()

# class star:
#     def __init__(self,name,galaxy):
#         self.name=name
#         self.galaxy=galaxy

#     def __str__(self):
#         return self.name  + ' in '+  self.galaxy
# sun = star("sun","milky way")
# print(sun)

# class vehicle:
#     pass
# class landvehicle(vehicle):
#     pass
# class trackedvehicle(landvehicle):
#     pass
# for cls1 in [vehicle,landvehicle,trackedvehicle]:
#     for cls2 in [vehicle,landvehicle,trackedvehicle]:
#         print(issubclass(cls1,cls2),end="\t")
#     print()

# class Super:
#     supvar =1

# class Sub(Super):
#     subvar = 2

# obj = Sub()
# print(obj.subvar)
# print(obj.supvar)

# class Super:
#     def __init__(self):
#         self.supVar = 11
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar =12
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# class level1:
#     variable_1=100
#     def __init__(self):
#         self.var_1=101
#     def fun_1(self):
#         return 102
    
# class level2(level1):
#     variable_2=200
#     def __init__(self):
#         super().__init__()
#         self.var_2=201
#     def fun_2(self):
#         return 202
# class Level3(level2):
#     variable_3=300
#     def __init__(self):
#         super().__init__()
#         self.var_3=301
#     def fun_3(self):
#         return 302
# obj=Level3()
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())


# class Exampleclasss:
#     def __init__(self,val=1):
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1
# example_object=Exampleclasss(8)
# try:
#     print("a-->",example_object.a)
# except AttributeError:
#     try:
#         print("b-->",example_object.b)
#     except AttributeError:
#         print("the error has occured! silently passing it!")



# class Exampleclasss:
    # a=1
#     def __init__(self,val=1):
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1
# example_object=Exampleclasss(8)

# if hasattr(example_object,'a'):
#     print("a=",example_object.a)

# if hasattr(example_object,'b'):
#     print("b=",example_object.b)

# print(hasattr(ExampleClass,'b'))
# print(hasattr(exampleClass,'a'))

# class python:
#     population=1
#     victims=0
#     def __init__(self):
#         self.length_ft=3
#         self.__venomous=False

# myobj=python()
# print("myobj.population",myobj.population)
# print("myobj.victims",myobj.victims)
# print("myobj.length_ft",myobj.length_ft)
# print("myobj.__venomous",myobj.__venomous)
# print("myobj.venomous",myobj._python__venomous)

# print(hasattr(version2,constructor))

# class Classy:
#     def visible(self):
#         print("visible")
#     def __hidden(self):
#         print("hidden")
# obj=Classy()
# obj.visible()
# try:
#     obj.__hidden()
# except:
#     print("failed")
# obj._Classy__hidden()#name mangling

# class Classy:
#     pass
# obj=Classy()
# print(type(obj))
# print(type(obj).__name__)

# class vehicle:
#     pass
# class landvehicle(vehicle):
#     pass
# class trackedvehicle(landvehicle):
#     pass
# my_vehicle=vehicle()
# my_land_vehicle=landvehicle=()
# my_tracked_vehicle=trackedvehicle()
# for obj in [my_vehicle,my_land_vehicle,my_tracked_vehicle]:
#     for cls in [vehicle,landvehicle,trackedvehicle]:
#         print(isinstance(obj,cls),end="\t")
#     print()

# class SampleClass:
#     def __init__(self,val):
#         self.val=val
# object_1=SampleClass(0)
# object_2=SampleClass(2)
# object_3= object_1
# object_3.val+=1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1="marry had a little "
# string_2="marry had a little lamb"
# string_1+="lamb"

# print(string_1==string_2,string_1 is string_2)

# class Super:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return "My name is" + self.name +"."
    
# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)
# # obj =Sub("isha")
# # print(obj)

# class SuperA:
#     var_a=10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b=20
#     def fun_b(self):
#         return 21
# class Sub(SuperA,SuperB):
#     pass
# obj =Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# class Level1:
#     var =100
#     def fun(self):
#         return 101
# class Level2:
#     var = 200
#     def fun(self):
#         return 202
# class Level3(Level2):
#     pass
# obj=Level3()
# print(obj.var,obj.fun())


# class Left:
#     var ="L"
#     var_left="LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var="R"
#     var_Right="RR"
#     def fun(self):
#         return "Right"
# class Sub(Left,Right):
#     pass
# obj=Sub()
# print(obj.var,obj.var_Right,obj.fun())
 
# class One:
#     def do_it(self):
#         print("do_it from One")
#     def doanything(self):
#         self.do_it() 
# class Two(One):    
#     def do_it(self):        
#         print("do_it from Two")
# one = One() 
# two = Two() 
# one.doanything()  
# two.doanything()

# def reciprocal(n):
#     try:
#         n=1/n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("its time to say goodbye")
#     return n 

# print("_________")
# print("reciprocal(2):",reciprocal(2))
# print("_________")
# print("reciprocal(0):",reciprocal(0))
# print("_________")


# try:
#     i=int("Hello")
# except Exception as e:
#     print(e)
#     print(e.__str__())

# class MyZeroDivisionError(ZeroDivisionError):
#     pass
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:
#         raise ZeroDivisionError("some bad news")
# do_the_division(False)
# do_the_division(True)

'''string'''
# city='Bhopal'
# print(city[0])
# print(city[2])
# print(city[-1])
# print(city[5])
# print(city[-3])
# print(city[3])

'''slicing in string'''
# name='priya sharma'
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])
# print(len(name))

'''upper and lower method'''
# text=' hello isha '
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.strip())
# print('isha'in text)
# print(text.find('isha'))
# print(text.count('isha'))

'''replacing element in string'''
# print(text.replace('isha','yash'))


'''split and join'''
# info='rahul,22,bhopal,engineer'
# parts=info.split(',')
# print(parts)
# rejoined='|'.join(parts)
# print(rejoined)

'''check content'''
# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('python'.isalpha())
# print(' '.isspace())

'''start/end check'''
# email='student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

'''Modern String Formatting Using F '''
# name,marks,rank ='isha',86.555,3
# print(f'hello,{name}!')
# print(f'marks:{marks:.2f}')
# print(f'marks:{marks:.0f}')
# print(f'count:{1000000:,}')

'''padding'''
# print(f'{name:<15}|{marks:>8.2f}|rank:{rank}')

'''expressions inside{}'''
# price,gst=500,0.18
# print(f'price:rs.{price}|gst:rs.{price*gst:.2f}|total:rs.{price*(1+gst):2f}')

'''problem to solve'''
# string ="hello ,how are you doing today?"
#count vowels in string
# count=0
# for char in string:
#     if char in "aeiou":
#         count+=1
# print(" vowels in this string:",count )

#print you from the string
# print(string.find("you"))      
# print(string[15:18])   
#      
#print the string in reverse order
# print(string[::-1])

# non_palin,palin = "abcdef","axttxa"
#check if the string is palindrome or not 
# word="abcdef"
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

# word="axttxa"
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

'''opening and closing of file/data'''
# with open("data.txt","r") as file:
#     data=file.read()
# print(data)

'''writing of data'''
# with open('student.txt','w') as f:
#     f.write('isha achhaniya,85,indore\n')
#     f.write('rishabh rai,82,indore\n')
#     f.write('harshita raghuwanshi,88,chhindwara\n')

# with open('student.txt','a')as f:
#     f.write('sneha joshi,77,bhopal\n')

# with open('student.txt','r')as f:
#     content=f.read()
# print(content)

'''line by line (efficient for large files)'''
# with open('student.txt','r')as f:
#     for line in f:
#         name,marks,city=line.strip().split(',')
#         print(f'{name:<15}|{marks:>5}|{city}')
#         print("-----------------------------")

'''CSV file processing'''
'''write'''
import csv 

# records = [
#     ['name','marks','city','grade'],
#     ['rahul','85','jabalpur','B'],    
#     ['priya','92','indore','A'],
#     ['amit','73','jabalpur','B']
# ]
# search_name=input("enter name :")
# found= False
# # with open('students.csv','w',newline='') as f:
# #     csv.writer(f).writerows(records)

'''read'''
# with open('students.csv','r',newline='') as f:
#     for row in csv.DictReader(f):
#     #     print(f'{row["name"]}:{row["marks"]}marks({"city"})')
    
#         if row["name"]==search_name:
#             print("record of student found")
#             print(row)
#             found = True
#             break 
# if not found:
#     print("Student not found")       

'''Numpy & Pandas'''
# import numpy as np 
# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[11,22,33],[22,33,44],[44,55,66]])
# arr3d = np.array([[[1,2,3],[2,3,4],[3,4,5]]])
# print(arr1d)
# print(arr2d.shape)
# print(arr2d.dtype)
# # print(arr2d.ndim)

# arr = np.empty((4, 3), dtype=np.int32)
# print(arr)

# zeros=np.zeros((3,4))
# print(zeros)
# ones=np.ones((2,5))
# print(ones)
# rng= np.arange(0,50,5)
# print(rng)

# lin = np.linspace(0,1,11)
# print(lin)

# arr = np.full((2, 2), 7)
# print(arr)
# random =np.random.randint(40,100,(5,3))
# print(random)
# identity_matrix = np.eye(3)
# diagonal= np.diag([1, 2, 3])

'''accessing elem in 1d array'''
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])

'''accesing elem in multi array'''
# arr=np.array([[2,3,4],[3,4,5],[4,5,6]])
# print(arr[1,2])

'''reshapping'''
# a = np.array([1, 2, 3, 4, 5, 6])
# r = a.reshape(2, 3)
# print(r)

'''stacking'''
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.stack((a, b), axis=0))
# print(np.stack((a, b), axis=1))

'''spiliting'''
# arr = np.arange(6)
# res = np.split(arr, 2)
# print(res)

'''common values (intersection) between two arrays'''
# A = np.array([1, 2, 3, 4, 5])
# B = np.array([3, 4, 5, 6, 7])
# common = np.intersect1d(A, B)
# print(common)

'''Broadcasting--allows us to perform arithmetic operations on arrays of different shapes without reshaping them. '''
# arr = np.array([10,20,30,40,50])
# print(arr*2)
# print(arr + 5)
# print(arr**2)

'''arithmetic operations'''
# a = np.array([5, 72, 13, 100])
# b = np.array([2, 5, 10, 30])
# res = np.add(a, b)
# print(res)

# a = np.array([5, 72, 13, 100])
# b = np.array([2, 5, 10, 30])
# res = np.subtract(a, b)
# print(res)

# a = np.array([5, 72, 13, 100])
# b = np.array([2, 5, 10, 30])
# res = np.multiply(a, b)
# print(res)

# a = np.array([5, 72, 13, 100])
# b = np.array([2, 5, 10, 30])
# res = np.divide(a, b)
# print(res)

# a = np.array([5, 72, 13, 100])
# b = np.array([2, 5, 10, 30])
# res = np.mod(a, b)
# print(res)

'''Statitics operations with numpy'''
# marks_2d =np.array([[85,90,78],[72,88,95],[91,76,83]])
# print(np.mean(marks_2d))
# print(np.mean(marks_2d,axis=1)) #mean per student(row)
# print(np.mean(marks_2d,axis=0)) #mean per subject(column)
# print(np.max(marks_2d))
# print(np.min(marks_2d))
# print(np.std(marks_2d))
# print(np.average(marks_2d))

'''matrix opr'''

# a = [[1, 2], [2, 3]]
# b = [[4, 5], [6, 7]]

# c = np.dot(a, b)
# print(c)

'''Printing greater numbers from list'''
# arr = np.array([55,82,43,91,67,78])
# print(arr[arr>70])

'''(.tolist())=checking array in list'''
# arr=np.array(
#     [
#         [1,2,3],[1,3,4],[4,5,3]
#         ]
#         )
# print(arr)
# print([1,2,3]in arr.tolist())
# print([2,3,4]in arr.tolist())


import pandas as pd

# data = {
#     'name':['harshi','isha','bhoomika','harshika'],
#     'age':[21,21,20,20],
#     'marks':[88,84,82,79],
#     'city':['cwara','indore','betul','indore']
# }
# df =pd.DataFrame(data)
# print(df)
# print(df.shape) #(5,4) 5 rows 4 columns
# print(df.head(3)) #first 3 rows
# print(df.dtypes) #data type
# print(df.describe()) #statistical summary

'''select columns'''
# print(df['name'])
# print(df[['name','marks']])

'''remove all rows containing NULL values from the original DataFrame.'''
# df = pd.read_csv('data.csv')
# df.dropna(inplace = True)
# print(df.to_string())

'''fill value in any empty space'''
# df = pd.read_csv('data.csv')
# df.fillna(130, inplace = True)
 
'''remove duplicates'''
# df.drop_duplicates(inplace = True)

'''filter rows'''
# print(df[df['marks'] >=80])
# print(df[df['city']=='indore'])
# print(df[(df['marks']>=80)&(df['city']=='indore')])

# def get_grade(x):
#     if x>=85:
#         return 'A'
#     elif x>=75:
#         return 'B'
#     else:
#         return 'c'
# df['grade']=df['marks'].apply(get_grade)
# print(df['grade'])
# print('-----------------------------')
# print(df)

'''Groupby '''
# city_avg =df.groupby('city')['marks'].mean()
# print(city_avg)

'''read real csv''' 

'''cleaning of data'''
# df2 = pd.read_csv('students.csv')
# df2 ['name'] = df2 ['name'].str.strip()
# print(df2)
# df2['marks'] = df2 ['marks'].str.replace ('#',' ')
# print(df2)
# df2['city'] = df2 ['city'].str.replace ('*',' ')
# print(df2)
# df2.to_csv('clean output.csv', index = False)

'''MatPlotLib'''
import matplotlib .pyplot as plt

# months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
# sales = [45,52,48,61,58,72,69,70,82,90,95,98]
# #line chart-trends over time
# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker='o',color='steelblue',linewidth=2,markersize=8)
# plt.fill_between(months,sales,alpha=0.15,color='steelblue')
# plt.title('monthly sales 2024(rs.thousand)',fontsize=14,fontweight='bold')
# plt.xlabel('month')
# plt.ylabel('sales (rs.k)')
# plt.grid(True,alpha=0.3)
# plt.tight_layout()
# plt.show()

'''program 2'''
# cities=['bhopal','indore','jabalpur','gwalior','ujjain']
# students=[1200,2800,980,850,650]
# colors=['#2196F3','#4CAF50','#FF9800','#9C27B0','#F44336']
# #
# plt.figure(figsize=(9,5))
# bars=plt.bar(cities,students,color=colors,edgecolor='white',linewidth=1.5)
# plt.title('student enrolled per city')
# plt.ylabel('number of students')
# for bar,val in zip(bars,students):
#     plt.text(bar.get_x()+bar.get_width()/2,val+30,str(val),ha='center',fontweight='bold')
# plt.tight_layout()
# plt.show()

import numpy as np 
'''scatter plot-relationship btw two variables'''
# study_hrs=np.random.uniform(2,10,50)
# marks= study_hrs*7+np.random.normal(0,8,50)
# marks= np.clip(marks,30,100)
# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn',s=100,alpha=0.8)
# plt.title('study hours vs exam marks')
# plt.xlabel('study hours/day')
# plt.ylabel('exam marks')
# plt.show()

import matplotlib.pyplot as plt

# marks = ['isha', 'harshi', 'khushi','anshi', 'bhoomika',]
# data = [23, 10, 35, 15, 12]

# plt.pie(data, labels=marks, autopct='%1.1f%%')
# plt.title(" Pie Chart of group of friends marks")
# plt.show()

'''seaborn'''

import seaborn as sns
import pandas as pd
import numpy as np

# np.random.seed(42)
#Data
# df=pd.DataFrame({
#     'marks':     np.random.randint(40,100,100),
#     'study_hours':  np.random.uniform(2,10,100),
#     'city':     np.random.choice(['bhopal','indore','jabalpur'],100),
#     'gender':   np.random.choice(['male','female'],100)})

'''histogram with kde-see the distibution'''
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'],bins=20,kde=True,color='steelblue')
# plt.title('distribution of student marks')
# plt.show()

'''sns.boxplot-outliners and spread per group'''
# sns.boxplot(data=df,x='city',y='marks',palette='Set3')
# plt.title('marks Distribution by city')
# plt.show()

'''heatmap(corelation)'''
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
# plt.title('correlation matrix')
# plt.show()

'''pair plot- all relations at once'''
# sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
study=np.random.uniform(2,10,60)
marks=np.random.normal(0,10,60)+study*8
marks=np.clip(marks,30,100)
absent=10-study+np.random.normal(0,1,60)
df=pd.DataFrame({
    'study_hours':study,
    'marks':marks,'absenses':absent})
corr_matrix=df.corr()
print(corr_matrix.round(2))
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',vmin=-1,vmax=1)
plt.title("correlation matrix")
plt.show()
