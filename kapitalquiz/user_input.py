player = input("Please enter your name: ")
print(f"Hello {player}!")
game_type = input("Please chose your game, do you want to guess countries, or capitals? \n")

valid_games = ["capital", "capitals", "countries", "country"]
score = 0
country_capitals = {"France": "Paris", "England": "London", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid"}

while game_type.lower() not in valid_games:
    print(game_type.lower())
    print("The category you chose is not valid! Please chose countries or capitals!")
    game_type = input()
else:
    print("Let the games begin!")

countries = []
capitals = []
items = country_capitals.items()
for i in items:
    countries.append(i[0])
    capitals.append(i[1])

# print(countries)
# print(capitals)


