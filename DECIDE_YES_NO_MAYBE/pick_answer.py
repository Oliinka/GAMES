import random


class AnswerPicker:
    answer = ("YES", "NO", "MAY BE")

    def __init__(self):
        pass

    def __str__(self):
        return f"The possible choices are: {self.answer}"

    def decide (self):
        return random.choice(self.answer)