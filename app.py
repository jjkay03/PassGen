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


# --------------------------------- Functions -------------------------------- #
# Function to change theme
def change_theme(theme):
    # Dark theme
    if theme=="dark":
        app.iconbitmap("assets/icon/icon-white.ico")  # Load icon
        ctk.set_appearance_mode("dark")  # Set ctk theme
        ctk.set_default_color_theme("green")  # Set default ctk color
        ttk.Style().theme_use("darkly-ctk")  # Set the ttkbootstrap theme
    
    # Light theme
    if theme=="light":
        app.iconbitmap("assets/icon/icon-black.ico")  # Load icon
        ctk.set_appearance_mode("light") # Set ctk theme
        ctk.set_default_color_theme("green")  # Set default ctk color
        ttk.Style().theme_use("litera-ctk")  # Set the ttkbootstrap theme


# ---------------------------------- Widgets --------------------------------- #



# ------------------------------------ Run ----------------------------------- #
change_theme("dark")  # Set default theme
app.mainloop()


# ----------------------------------- Test ----------------------------------- #
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()