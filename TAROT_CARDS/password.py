import random

class Password:
    # PASSWORD CHANGE IT IF YOU WANT TO
    current_password = "tarot"

    def access(self):
        # Get the length of the current password
        character_number = len(self.current_password)

        # Initialize a set to store chosen random numbers
        chosen_numbers = set()

        # Loop to ask for password characters
        for _ in range(3):
            # Generate a random number within the range of password characters
            random_number = random.randint(1, character_number)

            # Make sure the random number is not repeated
            while random_number in chosen_numbers:
                random_number = random.randint(1, character_number)

            # Add the chosen random number to the set
            chosen_numbers.add(random_number)

            # Ask the user to type the character at the randomly chosen position
            character = input(f"Type {random_number}. character of the password: ")

            # Check if the typed character is correct
            if character != self.current_password[random_number - 1]:
                print("Access denied!")
                return False  # If incorrect, deny access and return False
            else:
                continue

        # If the loop completes without returning False, grant access and return True
        return True