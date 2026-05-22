
def get_player_name():
    player = input("Please enter your name: ").strip()
    print(f"Hello {player}!")
    return player


def get_game_mode():
    valid_modes = {
        "1": "capital",
        "2": "country"
    }

    while True:
        game_type = input(
            "Please choose your game mode:\n"
            "1. Guess the CAPITAL based on the country\n"
            "2. Guess the COUNTRY based on the capital\n"
            "> "
        ).strip()

        if game_type in valid_modes:
            print("Let the games begin!")
            return valid_modes[game_type]

        print("Invalid choice! Please type 1 for 'capital' or 2 for 'country'.")




