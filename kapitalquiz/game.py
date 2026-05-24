from user_input import get_player_name, get_game_mode
from score_table import ScoreTable
from questions import QuestionRepo
from timed_input import timed_input


def play_mode(repo, mode, score_table):
    questions = repo.get_questions(mode)


    print(f"\n--- Starting {mode.upper()} mode ---\n")

    for q in questions:
        print(q.prompt)
        for idx, opt in enumerate(q.options, 1):
            print(f"{idx}. {opt}")

        answer, timed_out = timed_input("Your answer (1-4): ", timeout=10)

        if timed_out:
            print("\nTime's up! That counts as a wrong answer.\n")
            score_table.wrong_answers()
        else:
            if not answer.isdigit() or int(answer) not in range(1, 5):
                print("Invalid input! Counted as wrong.\n")
                score_table.wrong_answers()
            else:
                chosen = q.options[int(answer) - 1]
                if q.is_correct(chosen):
                    print("Correct!\n")
                    score_table.correct_answers()
                else:
                    print(f"Wrong! The correct answer was {q.correct_answer}\n")
                    score_table.wrong_answers()

            if score_table.wrong > 1:
                print("Too many wrong answers. Game over.\n")
                return False

            print(
                f"Current score: {score_table.correct} correct, {score_table.wrong} wrong\n")

    print(f"--- Finished {mode.upper()} mode ---\n")
    return True



def main():
    player_name = get_player_name()
    game_mode = get_game_mode()

    repo = QuestionRepo()
    score_table = ScoreTable(player_name)

    # Play the chosen mode first
    result = play_mode(repo, game_mode, score_table)

    if not result:
        print(f"Thanks for playing, {player_name}. Better luck next time!")
        # Print final summary
        summary = score_table.play_summary()
        print("\n===== FINAL SCORE =====")
        print(f"Player: {summary['Player']}")
        print(f"Correct answers: {summary['Correct answers']}")
        print(f"Wrong answers: {summary['Wrong answers']}")
        print(f"Score: {summary['Score']}")
        print(f"Date: {summary['Play time']}")
        print("=======================\n")
        return  # <-- stop the game completely

   # Determine the other mode
    other_mode = "country" if game_mode == "capital" else "capital"

    # Ask player if they want to continue
    while True:
        choice = input(f"Do you want to play the {other_mode.upper()} mode as well? (Y/N): ").strip().lower()

        if choice.lower() == "y":
            print(f"\nNow switching to {other_mode.upper()} mode!")
            play_mode(repo, other_mode, score_table)
            break

        elif choice.lower() == "n":
            print("\nCoward!")
            print(f"Ending game early. Thanks for playing {player_name}!\n")
            break

        else:
            print("Invalid input! Please type Y or N.")

    print(f"Great job, {player_name}!")

    # Print final summary
    summary = score_table.play_summary()
    print("\n===== FINAL SCORE =====")
    print(f"Player: {summary['Player']}")
    print(f"Correct answers: {summary['Correct answers']}")
    print(f"Wrong answers: {summary['Wrong answers']}")
    print(f"Score: {summary['Score']}")
    print(f"Date: {summary['Play time']}")
    print("=======================\n")

if __name__ == "__main__":
    main()