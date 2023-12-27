from fortune import TarotCardPicker
from pasword import Password

card = TarotCardPicker()
password= Password()

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

    choice_number = input("> ")

    if choice_number == "1":
        print(card.pick_one_card())

    elif choice_number == "2":
        print(card.three_cards_teller())

    elif choice_number == "3":
        print(card.card_meaning())

    elif choice_number == "4":
        print("For acces fill in pasword characters:")
        print(password.access())
        print(card.update_card_keywords())

    elif choice_number == "5":
        print("For access fill in password characters:")
        if password.access():
            result = card.update_card_meaning()
            print(result)

    elif choice_number == "6":
        card.save_to_csv()
        print("Changes saved. Exiting the program.")
        break

    else:
        print("Wrong choice! For exit press 6 and enter.")