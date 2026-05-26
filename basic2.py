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
    
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000) 
t2 = my_tuple * 3 
print(len(t2)) 
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
    