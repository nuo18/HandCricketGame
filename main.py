import randomize

isBatting = True
isOut = False
Total_First = 0
Total_Second = 0

# Toss methods
toss_win = randomize.toss()
# Checking whether user is batting or bowling
isBatting = randomize.choice(toss_win)