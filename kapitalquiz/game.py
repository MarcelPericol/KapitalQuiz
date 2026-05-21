from user_input import get_player_name, get_game_mode
from questions import QuestionRepo


def play_mode(repo, mode):
    questions = repo.get_questions(mode)
    wrong_answers = 0

    print(f"\n--- Starting {mode.upper()} mode ---\n")

    for q in questions:
        print(q.prompt)
        for idx, opt in enumerate(q.options, 1):
            print(f"{idx}. {opt}")

        answer = input("Your answer (1-4): ")

        # Invalid input counts as wrong
        if not answer.isdigit() or int(answer) not in range(1, 5):
            print("Invalid input → counted as WRONG.\n")
            wrong_answers += 1
        else:
            chosen = q.options[int(answer) - 1]
            if q.is_correct(chosen):
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer was {q.correct_answer}\n")
                wrong_answers += 1

        # Stop mode AND game if too many mistakes
        if wrong_answers > 1:
            print("Too many wrong answers. Game over.\n")
            return False   # <-- tell main() to stop the game

    print(f"--- Finished {mode.upper()} mode ---\n")
    return True  # <-- mode completed normally


def main():
    player_name = get_player_name()
    game_mode = get_game_mode()

    repo = QuestionRepo()

    # Play the chosen mode first
    result = play_mode(repo, game_mode)

    if not result:
        print(f"Thanks for playing, {player_name}. Better luck next time!")
        return  # <-- stop the game completely

    # Play the chosen mode first
    play_mode(repo, game_mode)

    # Determine the other mode
    other_mode = "country" if game_mode == "capital" else "capital"

    # Automatically start the other mode
    print(f"Now switching to {other_mode.upper()} mode!")
    play_mode(repo, other_mode)

    print("All questions in both modes have been completed!")
    print(f"Great job, {player_name}!")



if __name__ == "__main__":
    main()