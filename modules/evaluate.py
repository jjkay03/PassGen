# ---------------------------------------------------------------------------- #
#                            PassGen Evaluate Module                           #
# ---------------------------------------------------------------------------- #

# This module defines a PasswordEvaluator class that assesses the strength of a
# given password based on various criteria, including length and character
# complexity.

import string


# -------------------------- PasswordEvaluator Class ------------------------- #
class PasswordEvaluator:
    def __init__(self, password):
        """
        Initializes the PasswordEvaluator with the provided password.

        Parameters:
        - password (str): The password to be evaluated.
        """
        
        self.password = password

    # Evaluates the strength of the password and returns a strength grade
    def evaluate_strength(self):
        length_score = self._calculate_length_score()
        complexity_score = self._calculate_complexity_score()
        strength_score = length_score + complexity_score
        strength_grade = min(int((strength_score / self._max_strength_score()) * 100), 100)
        return strength_grade

    # Calculates the length-based score for the password
    def _calculate_length_score(self):
        return min(len(self.password) * 1.5, 40)

    # Calculates the complexity-based score for the password
    def _calculate_complexity_score(self):
        complexity_score = 0

        if any(char.isupper() for char in self.password):
            complexity_score += 2

        if any(char.islower() for char in self.password):
            complexity_score += 2

        if any(char.isdigit() for char in self.password):
            complexity_score += 1

        symbol_count = sum(1 for char in self.password if char in string.punctuation)
        complexity_score += min(symbol_count * 2, 10)

        return complexity_score

    # Returns the maximum possible strength score
    def _max_strength_score(self):
        return 30
