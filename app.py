# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk


# --------------------------------- Functions -------------------------------- #
# Function to change theme
def change_theme(theme):
    if theme=="dark":  # Dark theme
        app.iconbitmap("assets/icon/icon-white.ico")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
    if theme=="light":  # Light theme
        app.iconbitmap("assets/icon/icon-black.ico")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")


# ------------------------------------ App ----------------------------------- #
app = ctk.CTk()
app.title("PassGen")
app.geometry("800x500")
app.resizable(False, False)
change_theme("dark")  # Set default theme


# ---------------------------------- Widgets --------------------------------- #



# ------------------------------------ Run ----------------------------------- #
app.mainloop()


# ----------------------------------- Test ----------------------------------- #
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()