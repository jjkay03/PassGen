# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

import tkinter as tk
import customtkinter as ctk

# ----------------------------------- Setup ---------------------------------- #
# App
app = ctk.CTk()
app.title("PassGen")
app.geometry("800x500")
app.resizable(False, False)


# ---------------------------------- Widgets --------------------------------- #
# Main frames
frame_password = ctk.CTkFrame(app, corner_radius=10)
frame_evaluator = ctk.CTkFrame(app, corner_radius=10)
frame_customize = ctk.CTkFrame(app, corner_radius=10)

# Frame password
label_password_var = tk.StringVar(value=PasswordGenerator(length=15).generate_password())
label_password = ctk.CTkLabel(frame_password, textvariable=label_password_var, font=("Arial Bold", 25))


# ---------------------------------- Layout ---------------------------------- #
# Configure app grid
app.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
app.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

# Frame password
label_password.place(relx=0.02, rely=0.5, anchor="w")
frame_password.grid(column=0, row=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Frame evaluator
frame_evaluator.grid(column=4, row=0, sticky="nsew", padx=10, pady=10)

# Frame customize
frame_customize.grid(column=0, row=1, columnspan=5, rowspan=5, sticky="nsew", padx=10, pady=10)


# ------------------------------------ Run ----------------------------------- #
# Set default theme
ChangeTheme(app).set_dark_theme()

# Run the app
app.mainloop()


# ----------------------------------- Test ----------------------------------- #
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()