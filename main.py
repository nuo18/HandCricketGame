from randomize import *

batsman = 0
bowler = 0
isOut = False
total1 = 0
total2 = 0

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