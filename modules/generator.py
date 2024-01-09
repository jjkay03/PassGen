# ---------------------------------------------------------------------------- #
#                           PassGen Generator Module                           #
# ---------------------------------------------------------------------------- #

import string
import random


# -------------------------- PasswordGenerator Class ------------------------- #
class PasswordGenerator:
    def __init__(self, length, uppercase=True, lowercase=True, numbers=True, symbols=True, symbols_percentage=100):
        """
        Initialize the PasswordGenerator class with specified parameters.

        Parameters:
        - length (int): The length of the generated password.
        - uppercase (bool): Include uppercase letters in the password.
        - lowercase (bool): Include lowercase letters in the password.
        - numbers (bool): Include numbers in the password.
        - symbols (bool): Include symbols in the password.
        - symbols_percentage (int): Percentage of symbols to include in the password (default is 100%).
        """

        # Initialize parameters
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols
        self.symbols_percentage = symbols_percentage
    
    def generate_password(self):
        characters = ''

        # Include uppercase letters if specified
        if self.uppercase:
            characters += string.ascii_uppercase

        # Include lowercase letters if specified
        if self.lowercase:
            characters += string.ascii_lowercase

        # Include numbers if specified
        if self.numbers:
            characters += string.digits

        # Include symbols if specified
        if self.symbols:
            symbols = string.punctuation
            symbols_count = int((self.symbols_percentage / 100) * len(symbols))
            characters += symbols[:symbols_count]

        # Ensure at least one character type is selected
        if not any([self.uppercase, self.lowercase, self.numbers, self.symbols]):
            raise ValueError("At least one of uppercase, lowercase, numbers, or symbols should be True.")

        # Generate the password by randomly selecting characters from the combined set
        password = ''.join(random.choice(characters) for _ in range(self.length))
        
        return password
