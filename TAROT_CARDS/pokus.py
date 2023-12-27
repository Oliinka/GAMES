def update_card_meaning(self, card_name, new_meaning):
    card_name = card_name.lower()

    if card_name in self.tarot_card[self.card_name_col].str.lower().values:
        self.tarot_card.loc[
            self.tarot_card[self.card_name_col].str.lower() == card_name, self.meaning_col] = new_meaning
        return f"Card '{card_name}' meaning updated successfully."
    else:
        return f"Card '{card_name}' not found."