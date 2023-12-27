import pandas as pd
import random
class TarotCardPicker:

    def __init__(self, csv_file="tarot_cards.csv"):
        self.tarot_card = pd.read_csv(csv_file)
        self.card_name_col = "CardName"
        self.keywords_col = "Keywords"
        self.meaning_col = "Meaning"

    def pick_one_card(self):
        picked_card = random.choice(self.tarot_card[[self.card_name_col, self.keywords_col, self.meaning_col]].values)
        return f"""
    You picked: {picked_card[0]}
    Meaning of the cards: {picked_card[2]}
    Key words of the card: {picked_card[1]}"""

    def three_cards_teller(self):
        past_card = random.choice(self.tarot_card[[self.card_name_col, self.keywords_col, self.meaning_col]].values)
        present_card = random.choice(self.tarot_card[[self.card_name_col, self.keywords_col, self.meaning_col]].values)
        future_card = random.choice(self.tarot_card[[self.card_name_col, self.keywords_col, self.meaning_col]].values)

        past_info = f"""
    PAST: 
        The name of the card is: {past_card[0]}
        Meaning of the card is:  {past_card[2]} 
        Key words:               {past_card[1]}\n\n"""
        present_info = f"""
    PRESENT:
        The name of the card is: {present_card[0]} 
        Meaning of the card is:  {present_card[2]} 
        Key words:               {present_card[1]}\n\n"""
        future_info = f"""
    FUTURE: 
        The name of the card is: {future_card[0]} 
        Meaning of the card is:  {future_card[2]}
        Key words:               {future_card[1]}\n\n"""
        return f"{past_info}\n{present_info}\n{future_info}"



    def card_meaning(self):
        card_name = input("Search the card by its name: ")
        found_card = self.tarot_card[self.tarot_card[self.card_name_col].str.lower() == card_name.lower()]
        if not found_card.empty:
            matching_card = found_card.iloc[0]
            meaning = matching_card[self.meaning_col]
            keywords = matching_card[self.keywords_col]
            return f"""
Card Name: {matching_card[self.card_name_col]}
Meaning:   {meaning}
Keywords:  {keywords}"""
        else:
            return f"Card '{card_name}' not found."


    def update_card_keywords(self, card_name, new_keywords):
        card_name = card_name.lower()

        if card_name in self.tarot_card[self.card_name_col].str.lower().values:
            self.tarot_card.loc[self.tarot_card[self.card_name_col].str.lower() == card_name, self.keywords_col] = new_keywords
            return f"Card '{card_name}' keywords updated successfully."
        else:
            return f"Card '{card_name}' not found."

    def update_card_meaning(self):
        card_name = input("Enter the card name you want to update: ")
        found_card = self.tarot_card[self.tarot_card[self.card_name_col].str.lower() == card_name.lower()]

        if not found_card.empty:
            matching_card = found_card.iloc[0]
            current_meaning = matching_card[self.meaning_col]
            current_keywords = matching_card[self.keywords_col]

            print(f"""
    Card Name: {matching_card[self.card_name_col]}
    MEANING:   {current_meaning}
    Keywords:  {current_keywords}""")

            # Prompt user for new meaning
            new_meaning = input("Update the MEANING: ")

            # Update the meaning in the DataFrame
            self.tarot_card.loc[
                self.tarot_card[self.card_name_col].str.lower() == card_name, self.meaning_col] = new_meaning

            return f"Card '{card_name}' meaning updated successfully."
        else:
            return f"Card '{card_name}' not found."

    def save_to_csv(self):
        self.tarot_card.to_csv("tarot_cards.csv", index=False)
        return "Changes saved to tarot_cards.csv."