import random


class AnswerPicker:
    answer = ("YES", "NO", "MAY BE")

    def __init__(self):
        return f"The possible choices are: {self.answer}"
    def __int__(self):
        pass

    def decide (self):
        return random.choice(self.answer)