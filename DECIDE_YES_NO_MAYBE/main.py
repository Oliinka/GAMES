# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pick_answer import AnswerPicker

print("""
--------------------------------------------------------
ASK YOUR QUESTION! 
--------------------------------------------------------""")

answer_picker = AnswerPicker()

while True:
    print("""
1 - THINK OF THE QUESTION, PRESS "1" AND GET YOUR ANSWER
2 - NO MORE QUESTIONS? END THE PROGRAM BY PRESSING "2"  
3 - FIND OUT WHAT ARE THE POSSIBLE ANSWERS? PRESS "3"
--------------------------------------------------------
    """)

    choice_number = input("> ")

    # 1 pick random word from the list "answer" in the class AnswerPicker in the python file pick_answer.py
    if choice_number == "1":
        print(answer_picker.decide())

    # 2 exiting the program loop
    elif choice_number == "2":
        print("Exiting the program.")
        break  # Exit the loop and end the program

    elif choice_number == "3":
        print(answer_picker.__str__())

    else:
        print("Wrong choice! For exit press 2 and enter.")

