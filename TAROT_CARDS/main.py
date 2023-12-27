from fortune import TarotCardPicker
from password import Password
from datetime import datetime

# Create instances of the TarotCardPicker and Password classes
card = TarotCardPicker()
password = Password()

print("""
-------------------------------------------------------
WELCOME TO TAROT READING
--------------------------------------------------------""")

while True:
    print("""
1 - ONE CARD READING
    think of your problem and get the advice or answer
    with one card reading by pressing "1"
2 - THREE CARDS READING
    think of your situation and get the advice or answer
    with three cards reading by pressing "2"
3 - FIND OUT WHAT IS MEANING OF THE CARD, PRESS "3"
4 - UPDATE KEY WORDS 
    to update key words press "4" 
5 - UPDATE THE MEANING
    to update description press "5"
6 - SAVE CHANGES AND EXIT
    to save changes and exit press "6"
--------------------------------------------------------
    """)

    # Get the user's choice
    choice_number = input("> ")

    # Perform actions 1-6 based on the user's choice
    if choice_number == "1":
        # Option 1: One Card Reading picks one random card from the CSV FILE
        print(card.pick_one_card())

    elif choice_number == "2":
        # Option 2: Three Cards Reading picks three random cards from the CSV FILE
        print(card.three_cards_teller())

    elif choice_number == "3":
        # Option 3: Fill in name of the tarot card and find Out Meaning of the Card
        print(card.card_meaning())

    elif choice_number == "4":
        # Option 4: Update Key Words of the card
        print("For access, fill in password characters:")
        # Check password and perform action if access is granted
        if password.access():
            print(card.update_card_keywords())

    elif choice_number == "5":
        # Option 5: Update the Meaning of the card
        print("For access, fill in password characters:")
        # Check password and perform action if access is granted
        if password.access():
            result = card.update_card_meaning()
            print(result)

    elif choice_number == "6":
        # Option 6: Save Changes and Exit
        card.save_to_csv()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Changes saved. Exiting the program at {current_time}.")
        break

    else:
        # Handle invalid choices
        print("Wrong choice! For exit, press 6 and enter.")