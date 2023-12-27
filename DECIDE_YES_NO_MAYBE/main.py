# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pick_answer import AnswerPicker:

print("""
-------------------------------------
ASK YOUR QUESTION! 
-------------------------------------""")

answer_picker = AnswerPicker()

while True:
    print("""
    Choose one of the following:
    1 - GET YOUR ANSWER
    2 - end the program
    --------------------------------------
    """)

    choice_number = input("> ")

#5 searches ensurer by its age
    if choice_number == "1":
        print(found_insurer)


#9 exiting the program loop
    elif choice_number == "9":
        print("Exiting the program.")
        break  # Exit the loop and end the program

    else:
        print("Wrong choice! For exit press 9 and enter.")