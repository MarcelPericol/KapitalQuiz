from random import random

from user_input import *

valid_games = ["capital", "capitals", "countries", "country"]
score = 0
country_capitals = {"France": "Paris", "England": "London", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid"}

while game_type.lower() not in valid_games:
    print(game_type.lower())
    print("The category you chose is not valid! Please chose countries or capitals!")
    game_type = input()
else:
    print("Let the games begin!")

for i in range(len(country_capitals)):
    print()
print(len(country_capitals))