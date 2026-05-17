import random

def guessNum():
    randnum = random.randint(1,10)
    while(True):
        num = int(input())
        if (num == randnum):
            print("You gussed it right!!!")
            return True
        print("Close...  Try again...")

print("Enter the number between 1 to 10: ")
guessNum()