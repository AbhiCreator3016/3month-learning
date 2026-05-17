import random

def Winner(teams):
    winTeam=random.choice(teams)
    return winTeam

print("Guess the winner : ")
teams = ["Rajasthan Royals","GT","PK"]
print(Winner(teams))