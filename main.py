import randomize
import innings

isBatting = True
isOut = False
Total_First = 0 # First inning total
Total_Second = 0 # Second inning total

# Toss methods
toss_win = randomize.toss()
# Checking whether user is batting or bowling
isBatting = randomize.choice(toss_win)

if(isBatting == True):
    # First inning
    innings.first_batting(isBatting)
else:
    pass