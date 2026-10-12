import random

n = random.randint(1,101)

diff = int(input('''Choose the difficulty:  for easy write 1 
                        for normal write 2
                        for hard write  3  :  '''))
if diff == 1:
    print("You got scared and choose easy mode")
    chances = 20
elif diff == 2:
    print("You choose to play the normal mode")
    chances = 10
elif diff == 3:
    print("You choose hard! brave of you")
    chances = 7

print(f"You have {chances} chances to guess a number")

for i in range(1, chances+1):
    guess = int(input("guess the number : "))
    if guess == n:
        print("yep you got it ")
        break
    elif i < chances:
        if guess > n:
            print("try lower")
        elif guess < n:
            print("try higher")
    elif i == chances:
        print(f"you lost, the number was {n}")
