import random

def toss():
    print("Press 1 for Heads and 2 for tails. ")
    user_toss = int(input())
    comp_gen = random.randint(1, 2)
    if(user_toss == comp_gen):
        print("You won the toss!")
        return True
    else:
        print("You lost the toss!")
        return False

def choice(toss_win):
    if(toss_win == True):
        print("Press 1 to bat and 2 to Bowl.")
        user_choice = int(input())
        if(user_choice == 1):
            print("You choose to Bat.")
            return True
        else:
            print("You choose to Bowl.")
            return False
    else:
        computer_choice = random.randint(1, 2)
        if(computer_choice == 1):
            print("Computer choose to Bat.")
            print("You will Bowl now.")
            return False
        else:
            print("Computer choose to Bowl.")
            print("You will Bat now.")
            return True

