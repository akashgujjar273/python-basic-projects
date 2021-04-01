opt=['rock','paper','siccors']
from random import randint
computer=opt[randint(0,2)]
print(computer)

player=False

while player==False:
    player=input("rock, paper, siccors"'\n')
    if player==computer:
        print("Tie")
    elif player=="rock":
        if computer=="siccors":
            print("You Win")
        else:
            print("You lose")
    elif player=="paper":
        if computer=="rock":
            print("You Win")
        else:
            print("You lose")
    elif player=="siccors":
        if computer=="paper":
            print("You Win")
        else:
            print("You lose")
    else:
        print("please enter correct")

