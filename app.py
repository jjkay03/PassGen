# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

# ----------------------------------- Setup ---------------------------------- #
# App
app = ctk.CTk()
app.title("PassGen")
app.geometry("800x500")
app.resizable(False, False)

# Load custom ttkb themes
ttk.Style().load_user_themes(file="assets/themes/ttkb-themes.json")  


# ---------------------------------- Widgets --------------------------------- #



# ------------------------------------ Run ----------------------------------- #
ChangeTheme(app).set_dark_theme()
app.mainloop()


# ----------------------------------- Test ----------------------------------- #
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()