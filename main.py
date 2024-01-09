# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

password_generator = PasswordGenerator(
    length=15, 
    uppercase=True, 
    lowercase=True, 
    numbers=True, 
    symbols=True, 
    symbols_percentage=100
    )

generated_password = password_generator.generate_password()

print()
print("Generated Password:", generated_password)
print()
