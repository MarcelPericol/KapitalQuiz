
def get_player_name():
    player = input("Please enter your name: ").strip()
    print(f"Hello {player}!")
    return player


def get_game_mode():
    valid_modes = {
        "capital": "capital",
        "capitals": "capital",
        "country": "country",
        "countries": "country"
    }

    while True:
        game_type = input(
            "Please choose your game mode:\n"
            "Do want to guess capitals?\n"
            "Do you want to guess countries?\n"
            "> "
        ).lower().strip()

        if game_type in valid_modes:
            print("Let the games begin!")
            return valid_modes[game_type]

        print("Invalid choice! Please type 'capital' or 'country'.")

score = 0



