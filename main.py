# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

password_generator = PasswordGenerator(
    length=10, 
    uppercase=False, 
    lowercase=True, 
    numbers=False, 
    symbols=False, 
    symbols_percentage=100
    )

generated_password = password_generator.generate_password()
password_grade = PasswordEvaluator(generated_password).evaluate_strength()

print()
print("Generated Password:", generated_password)
print("Password Grade:", password_grade)
print()

