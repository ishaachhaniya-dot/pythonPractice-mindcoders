# # numbers = [10,5,7,2,1]
# # print(numbers)
# # print(type(numbers))

# # why list starts from 0 in python 
# # numbers[0]=> numbers address +((number of bytes occupied * index)) //answer 1st pos
# # numbers[1]=> numbers address +((number of bytes occupied * index)) //answer 2nd pos
# # numbers[2]=> numbers address +((number of bytes occupied * index))  // answer 3rd pos

# # numbers =[]
# # numbers =[2,3,4,5]
# # print("list contents",numbers)

# # print("first element",numbers[0])
# # print("second element",numbers[1])
# # print("third element",numbers[2])

# # numbers[0] = 22
# # print("numbers[0]",numbers[0])
# # print(numbers)

# # numbers[1]=numbers[3]
# # print(numbers)

# # print(len(numbers))
# # del numbers[2]
# # print(numbers)
# # print(numbers[-1])
# # print(numbers[-3])
# # print(numbers[-4]) //out of range

# # //practice question
# # list =[1,2,3,4,5]
# # print(len(list))
# # del list[4]
# # print(len(list))
# # i= int(input("enter the number:"))
# # list[int(len(list)//2)]=i
# # # print(list)
# # list =[1,2,3,4,5]
# # print(list)
# # list.insert(0,3)    
# # print(list)

# # my_list = [1,2,3,4,5,6,7,8,9]
# # for count in range(len(my_list)):
# # print

# # n=int(input("enter number:"))
# # i=1
# # total=0
# # while i<=n:
# #     total+=i
# #     i+=1
# # print(total)


# # numbers=[1,2,3,4,5]
# # numbers.append(6)
# # print(numbers)

# # rishabh
# # my_list = [8, 10, 6, 2, 4]
# # print(my_list) 
# # count = 0
# # for i in range(len(my_list)):
# #     for j in range(i + 1, len(my_list)):
# #         count += 1
# #         if my_list[i] > my_list[j]:
# #             my_list[i], my_list[j] = my_list[j], my_list[i] 
# # print(my_list)
# # print(count)

# # sirr
# # my_list=[1,2,3,4,5]
# # # my_list=[8,10,6,2,4]
# # swapped= True
# # count=0
# # index=0
# # while swapped:
# #     swapped= False 
# #     for i in range(len(my_list)-1-index):
# #          count+=1
# #          if my_list[i]>my_list[i+1]:
# #             swapped = True
# #             my_list[i],my_list[i+1]= my_list[i+1],my_list[i]
# # print(my_list)
# # print(count)


# # my_list = [8, 10, 6, 2, 4] 
# # my_list.sort() 
# # print(my_list)
# # my_list.reverse()
# # print(my_list)

# # my_list = [10, 8, 6, 4, 2] 
# # new_list = my_list[1:3]
# # print(new_list)

# # my_list = [10, 8, 6, 4, 2] 
# # new_list = my_list[1:-1]
# # print(new_list)

# # my_list = [10, 8, 6, 4, 2] 
# # new_list = my_list[-1:1] 
# # print(new_list)

# # my_list = [10, 8, 6, 4, 2] 
# # new_list = my_list[:3] 
# # print(new_list)

# # my_list = [10, 8, 6, 4, 2] 
# # new_list = my_list[3:] 
# # print(new_list)

# # my_list = [10, 8, 6, 4, 2] 
# # del my_list[1:3] 
# # # print(my_list)


# # # my_list = [10, 8, 6, 4, 2] 
# # # del my_list[:] 
# # # print(my_list)

# # # row=[]
# # # for i in range(8):
# # #     row.append("WHITE_PAWN")
# # # print(row)

# # # row=["WHITE_PAWN" for i in range(8)]
# # # print(row)

# # # squares=[ x **2 for x in range(10)]
# # # print(squares)

# # # twos=[2** index for index in range(10)]
# # # print(twos)

# # # squares = [index ** 2 for index in range(10)]
# # # # odds=[index for index in squares if index %2 != 0]
# # # # print(odds) 

# # # even = [index for index in squares if index %2 ==0]
# # # # print(even)

# # # board =[]
# # # for i in range(8):
# # #     row =["EMPTY" for i in range(8)]
# # #     board.append(row)

# # board = []
# # for i in range(8):
# #      row = ["EMPTY" for i in range(8)]  
# #      board.append(row)

# # print(board)

     
# # board[0][0]="ROOK"
# # board[0][7]="ROOK"
# # board[7][0]="ROOK"
# # board[7][7]="ROOK"

# # # print("------------")

# # # for element in board:
# # #     print(element)

# # # board[0][1]="KNIGHT"
# # # board[0][6]="KNIGHT"
# # # board[7][1]="KNIGHT"
# # # board[7][6]="KNIGHT"
# # # print("------------")
# # # for element in board:
# # #     print(element)

# # temps = [[0.0 for h in range(24)] for d in range(31)]
# # temp1 = 19
# # temp2 = 32
# # count = 0


# # for days in temps:
# #     if count== 0:
# #         days[11]=temp1
# #         count = 1
# #     else:
# #         days[11]= temp2
# #         count=0

# # for element in temps:
# #     print(element)

# # total=0.0
# # for days in temps:
# #     total+=days[11]
# # average = total/31
# # print("Average temperature at noon:",average)

# # highest = -100.0 
# # for day in temps:
# #      for temp in day:
# #         if temp > highest:
# #             highest = temp
# # print("Highest temp:",highest)


# # hot_days=0
# # for day in temps:
# #     if day[11]>20.0:
# #         hot_days +=1
# # print(hot_days,"days were hot")

# # rooms = [[[False for r in range(20)] for f in range(15)]for t in range(3)]
# # print(rooms)

# # rooms[1][9][13] = True
# # rooms[0][4][1]= True

# # vacancy=0
# # for room_number in range(20):
# #     # if not rooms[2][14][room_number]:
# #     if not rooms[1][9][room_number]:

# #         vacancy+=1
# # print("vacancy in 3rd 15th floor",vacancy)


# # def scope_test():
# # x = 123
# # scope_test()
# # print(x)


# # def my_function():
# #     print("DO i know that varible",var)

# # var =1
# # my_function()
# # print(var)


# # def my_function():
# #     global var
# #     var =2
# #     print("DO i know that variable",var)

# # var =1
# # my_function
# # print(var)


# # def my_function():
# #     global var
# #     var =5
# #     return var
# # print(return_var())
# print(var)

# def my_function(n):
#     print("I got",n)
#     n+=1
#     print("I have",n)

# var =1
# my_function(var)
# print(var)

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


class Exampleclasss:
    def __init__(self,val=1):
        if val%2!=0:
            self.a=1
        else:
            self.b=1
example_object=Exampleclasss(8)
try:
    print("a-->",example_object.a)
except AttributeError:
    try:
        print("b-->",example_object.b)
    except AttributeError:
        print("the error has occured! silently passing it!")