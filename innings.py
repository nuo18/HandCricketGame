import random
import time

def first_batting(isBatting):
    user_score = 0
    user_cur = 0
    comp_bowl = 0
    print("Enter between 1 to 6.")
    
    while(isBatting):
        pause()
        space()
        print("Enter: ")
        user_cur = int(input()) # User inputs batting choice
        comp_bowl = random.randint(1,6) # Computes random bowl number from 1-6
        pause()
        if(user_cur == comp_bowl):
            print("You are out!")
            print("You scored a total of "+str(user_score)+" runs.")
            isBatting = False
        else:
            print("Computer bowled: "+str(comp_bowl))
            user_score = user_score + user_cur # current runs are added to total
            print("Total Runs: "+str(user_score))
    
    space()
    print("First inning total: " + str(user_score))
    print("Need to defend: " + str(user_score + 1))
    space()
    space()
    
    user_score = user_score+1
    comp_score = 0
    # checking whether the computer has crossed the user's score
    while(comp_score <= user_score):
        pause()
        space()
        print("Enter: ")
        user_cur = int(input()) # User inputs bowling choice
        comp_bowl = random.randint(1,6) # Computes random bat number from 1-6
        pause()
        if(user_cur == comp_bowl):
            print("The computer is out! ")
            print("It scored a total of "+str(comp_score)+" runs.")
            print("You won by "+str(user_score-comp_score))
            print("GGs")
            break
        elif(comp_score > user_score):
            print("Computer batted: "+str(comp_bowl))
            print("Total Runs: "+str(comp_score))
            print("You lost! GGs")
        else:
            print("Computer batted: "+str(comp_bowl))
            comp_score = comp_score + comp_bowl # current runs are added to total
            print("Total Runs: "+str(comp_score))
    space()
    space()
    print("Thanks for playing!")
    
            
        

def pause():
    time.sleep(1)

def space():
    print("---------")


def second_batting(isBatting):
    comp_score = 0
    comp_random = 0
    user_cur = 0
    print("Enter between 1 to 6.")
    
    while(not isBatting):
        pause()
        space()
        print("Enter: ")
        user_cur = int(input())
        comp_random = random.randint(1,6)
        pause()
        if(user_cur == comp_random):
            print("")