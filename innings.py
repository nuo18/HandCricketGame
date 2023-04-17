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
            print("The computer scored a total of "+str(comp_score)+" runs.")
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
            print("The computer is out!")
            print("The computer scored a total of: "+str(comp_score))
            isBatting = True
        else:
            print("The Computer hit: "+str(comp_random))
            comp_score = comp_score + comp_random # current runs are added to total
            print("Total: "+str(comp_score))
        
    space()
    print("First innings total: " + str(comp_score))
    comp_score = comp_score + 1
    print("Need to score: "+ str(comp_score)) # adds one to total because of first innings run
    space()
    space()
    isBatting = True
        
    user_score = 0 # resets random number generator to start of loop for next user input
    while(comp_score >= user_score):
        pause()
        space()
        print("Enter:")
        user_cur = int(input()) # input is converted to an int for comparison later on to see if user hit a bat or bowl
        comp_random = random.randint(1,6) # resets random number generator for next user input to start of loop for next user input
        pause()
        if(user_cur == comp_random):
            print("The computer threw a: "+str(comp_random))
            print("You are out! ")
            print("You scored a total of: "+str(user_score)) # user wins the game and scored a total of the user's runs
            print("The computer won by "+str(comp_score - user_score)+" runs") # comp wins by the number of runs scored by user, minus the number of runs scored by user, wins the game
            print("GGs")
            break
        else:
            print("Computer bowled: "+str(comp_random))
            user_score = user_score + user_cur
            print("Total Runs: "+str(user_score))
            print("More "+str(comp_score-user_score)+" needed to win")
        
        if(user_score > comp_score):
            print("The Computer bowled: "+str(comp_random))
            print("Total runs: "+str(user_score))
            print("You won! GGs")
            break
    
    space()
    space()
    print("Thanks for playing!")
        