'''rock paper scissor'''

import random
print("welcome to rock paper scissors game")

choices =["rock","paper","scissors"]

user = input("Enter rock, paper or scissor of theese : ").lower()
computer= random.choice(choices)

print("computer",computer)

if user==computer:
    print("it is a tie")
elif user=="rock" and computer=="scissors"or\
    user=="paper" and computer=="rock"or\
    user =="scissors" and computer=="paper":
    print("you win")
else:
    print("computer win")