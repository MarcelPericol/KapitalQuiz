import json
import sqlite3
import random
from pathlib import Path


class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer == self.correct_answer

def generate_options(correct_answer, all_answers, num_options=4):
    """Generate multiple-choice options."""
    distractors = [a for a in all_answers if a != correct_answer]
    selected = random.sample(distractors, num_options - 1)
    options = selected + [correct_answer]
    random.shuffle(options)
    return options

class QuestionRepo:
    def __init__(self, filepath = None):
        if filepath is None:
            base = Path(__file__).resolve().parents[1]
            filepath = base / "Database" / "questions.json"

        self.filepath = filepath
        self.data = self._load_data()

    def _load_data(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def get_questions(self, mode):
        """
               mode = 'capital'   → Guess the capital
               mode = 'country'   → Guess the country
               """
        questions = []

        for country , capital in self.data.items():
            if mode == "capital":
                prompt = f"What is the capital of {country}?"
                correct = capital
                all_answers = list(self.data.values())
            else:
                prompt = f"{capital} is the capital of which country?"
                correct = country
                all_answers = list(self.data.keys())

            options = generate_options(correct, all_answers)
            questions.append(Question(prompt, options, correct))

        return questions


