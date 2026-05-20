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

# rishabh
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

# sirr
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


# my_list = [8, 10, 6, 2, 4] 
# my_list.sort() 
# print(my_list)
# my_list.reverse()
# print(my_list)

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

list=[1,2,3,4,5]
print(5 not in the list)