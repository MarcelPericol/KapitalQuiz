from datetime import datetime


class ScoreTable:
    def __init__(self, player):
        self.player_name = player
        self.correct = 0
        self.wrong = 0
        self.play_time = datetime.now()

    def correct_answers(self):
        self.correct += 1

    def wrong_answers(self):
        self.wrong += 1

    def total_score(self):
        return self.correct

    def play_summary(self):
        return {
            "Player": self.player_name,
            "Correct answers": self.correct,
            "Wrong answers": self.wrong,
            "Score": self.total_score(),
            "Play time": self.play_time.strftime("%Y-%m-%d %H:%M:%S")
        }