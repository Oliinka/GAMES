import pandas as pd
import random

class TarotCardPicker:
    # Constructor to initialize the TarotCardPicker instance
    def __init__(self, csv_file="tarot_cards.csv"):
        # Read the CSV file into a DataFrame
        self.tarot_card = pd.read_csv(csv_file)
        # Define column names
        self.card_name_col = "CardName"
        self.keywords_col = "Keywords"
        self.meaning_col = "Meaning"

    # Method to pick one card randomly
    def pick_one_card(self):
        # Choose a random card from the DataFrame
        picked_card = random.choice(self.tarot_card[[self.card_name_col, self.keywords_col, self.meaning_col]].values)
        return f"""
    You picked: {picked_card[0]}
    Meaning of the cards: {picked_card[2]}
    Key words of the card: {picked_card[1]}"""

    # Method for a three-card reading
    def three_cards_teller(self):
        # Choose random cards for past, present, and future
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

    # Method to find the meaning of a specific card
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

    # Method to update keywords of a specific card
    def update_card_keywords(self):
        card_name = input("Enter the card name you want to update: ")
        found_card = self.tarot_card[self.tarot_card[self.card_name_col].str.lower() == card_name.lower()]

        if not found_card.empty:
            matching_card = found_card.iloc[0]
            current_meaning = matching_card[self.meaning_col]
            current_keywords = matching_card[self.keywords_col]

            print(f"""
    Card Name: {matching_card[self.card_name_col]}
    Meaning:   {current_meaning}
    KEYWORDS:  {current_keywords}""")

            # Prompt user for new keywords
            new_keywords = input("Update the KEYWORDS: ")

            # Update the keywords in the DataFrame
            self.tarot_card.loc[self.tarot_card[self.card_name_col].str.lower() == card_name, self.keywords_col] = new_keywords

            return f"Card '{card_name}' keywords updated successfully."
        else:
            return f"Card '{card_name}' not found."

    # Method to update the meaning of a specific card
    def update_card_meaning(self):
        # Input of the card I want to search
        card_name = input("Enter the card name you want to update: ")

        # Find the card in the DataFrame based on the input card_name
        found_card = self.tarot_card[self.tarot_card[self.card_name_col].str.lower() == card_name.lower()]

        # Check if the card is found
        if not found_card.empty:
            # Get the first matching card (assuming there's no duplicate card names)
            matching_card = found_card.iloc[0]
            current_meaning = matching_card[self.meaning_col]
            current_keywords = matching_card[self.keywords_col]

            # Display the current card information
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
            # Card not found, provide an appropriate message
            return f"Card '{card_name}' not found."

    # Method to save changes to the CSV file
    def save_to_csv(self):
        self.tarot_card.to_csv("tarot_cards.csv", index=False)
        return "Changes saved to tarot_cards.csv."