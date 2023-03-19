from randomize import *

batsman = 0
bowler = 0
isOut = False
isBatting = False
total1 = 0
total2 = 0
choice = 0

print("Welcome to the Game of HandCricket.\nYou will play against the computer.")
print("Toss!")
print("Press 0 of heads, or 1 for tails. ")
coin = input()

if(coin == toss):
    print("You won the toss. Select 0 to Bat, or 1 to Bowl. ")
    choice = input()
    if(choice == 0):
        print("You choose to Bat first. ")
        isBatting = True
    else:
        print("You choose to bowl first. ")
        isBatting = False
else:
    if(toss == 0):
        print("Computer choose to Bowl first. ")
        isBatting = True
    else:
        print("Computer choose to Bat first. ")
        isBatting = False
        
    


def user_bats(  ):
    print("You are batting: ")
    while(isOut!=True):
        print("Enter: ")
        batsman = int(input())
        bowler = bowl()
    
        if(batsman == bowler):
            print("You are out!")
            print("You scored: "+str(total1)+" runs.")
            print("\n\n---------\n\n")
            isOut = True
        else:
            print("You hit "+str(batsman)+" runs.")
            total1+=batsman
            print("Current Score: "+str(total1))
            print("\n---------\n")

print("You are bowling: ")
isOut = False
while(isOut!=True):
    print("Enter: ")
    bowler = int(input())
    batsman = bat()
    
    if(total2 > total1):
        print("You lost the game!")
        print("Try again.")
        isOut = True
    else:
        if(bowler == batsman):
            print("You won the game!")
            print("You won by "+str(total1-total2))
            isOut = True
        else:
            print("Computer hit "+str(batsman)+" runs.")
            total2+=batsman
            print("More "+str(total1-total2)+" runs to win.")
            print("\n---------\n")