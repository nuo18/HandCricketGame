import random
import time

def first_batting(isBatting):
    user_score = 0
    user_cur = 0
    comp_bowl = 0
    print("Enter between 1 to 6.")
    
    while(isBatting):
        pause()
        print("-----")
        print("Enter: ")
        user_cur = int(input()) # User inputs batting choice
        comp_bowl = random.randint(1,6) # Computes random bowl number from 1-6
        pause()
        if(user_cur == comp_bowl):
            print("You are out!")
            print("You scored a total of "+str(user_score)+" runs.")
            isBatting = False
        else:
            print("Computer selected: "+str(comp_bowl))
            user_score = user_score + user_cur # current runs are added to total
            print("Total Runs: "+str(user_score))
    
    print("-----")
    print("First inning total: " + str(user_score))
    print("Need to defend: " + str(user_score + 1))
    print("-----")
    
    user_score = user_score+1

def pause():
    time.sleep(1)