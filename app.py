# ---------------------------------------------------------------------------- #
#                                    PassGen                                   #
# ---------------------------------------------------------------------------- #

from modules import *  # Import all custom modules in /modules dir

import tkinter as tk
import customtkinter as ctk
from PIL import Image
import pyperclip


# ----------------------------------- Setup ---------------------------------- #
# App
app = ctk.CTk()
app.title("PassGen")
app.geometry("800x500")
app.resizable(False, False)


# --------------------------------- Variable --------------------------------- #
# Variables
password = "Password"

# Tk variables
password_tkvar = tk.StringVar(value=password)
password_length_tkvar = tk.IntVar(value=15)
password_uppercase_tkvar = tk.BooleanVar(value=True)
password_lowercase_tkvar = tk.BooleanVar(value=True)
password_numbers_tkvar = tk.BooleanVar(value=True)
password_symbols_tkvar = tk.BooleanVar(value=True)

btn_img_generate = ctk.CTkImage(
    light_image=Image.open("assets/buttons/generate-black.png"),
    dark_image=Image.open("assets/buttons/generate-white.png"),
    size=(30,30)
)
btn_img_copy = ctk.CTkImage(
    light_image=Image.open("assets/buttons/copy-black.png"),
    dark_image=Image.open("assets/buttons/copy-white.png"),
    size=(30,30)
)


# --------------------------------- Functions -------------------------------- #
# Function that generates password and update app
def generate_password():
    global password

    # Generate password using generator module
    password = PasswordGenerator(
        length=password_length_tkvar.get(),
        uppercase=password_uppercase_tkvar.get(),
        lowercase=password_lowercase_tkvar.get(),
        numbers=password_numbers_tkvar.get(),
        symbols=password_symbols_tkvar.get()
    ).generate_password()

    # Get password grade using evaluate module
    password_grade = PasswordEvaluator(password).evaluate_strength()
    
    # Determine progress bar color
    if password_grade <= 20:
        progressbar_color = "#e74c3c"
    if password_grade >= 20:
        progressbar_color = "#f36512"
    if password_grade >= 40:
        progressbar_color = "#ffbd2e"
    if password_grade >= 60:
        progressbar_color = "#92c934"
    if password_grade >= 80:
        progressbar_color = "#59c934"

    # Update widgets
    password_tkvar.set(password)
    progressbar_password.set(password_grade/100)
    progressbar_password.configure(progress_color=progressbar_color)

    print()
    print("PASSWORD:", password)
    print("GRADE:", password_grade)

    return password


# ---------------------------------- Widgets --------------------------------- #
# Frame password
frame_password = ctk.CTkFrame(app, corner_radius=10)
label_password = ctk.CTkLabel(frame_password, textvariable=password_tkvar, font=("Arial", 25))
progressbar_password = ctk.CTkProgressBar(frame_password, height=10, width=785, progress_color="#59c934", fg_color="")
button_password_1 = ctk.CTkButton(frame_password, image=btn_img_generate, height=30, width=20, hover_color=("#c9c9c9","#242424"), corner_radius=20 , fg_color="transparent", text="", command=generate_password)
button_password_2 = ctk.CTkButton(frame_password, image=btn_img_copy, height=30, width=20, hover_color=("#c9c9c9","#242424"), corner_radius=20, fg_color="transparent", text="", command=(lambda: pyperclip.copy(password)))

# Frame customize
frame_customize = ctk.CTkFrame(app, corner_radius=10)
label_customize_1 = ctk.CTkLabel(frame_customize, text="Customize Password", font=("Arial Bold", 20))
label_customize_2 = ctk.CTkLabel(frame_customize, text="Password Length", font=("Arial", 18))
label_customize_3 = ctk.CTkLabel(master=frame_customize, textvariable=password_length_tkvar, corner_radius=5, fg_color=("#c9c9c9","#242424"), font=("Arial", 18))
slider_customize = ctk.CTkSlider(master=frame_customize, from_ = 1, to = 40, width=300, variable=password_length_tkvar, progress_color="#59c934", button_color="#429526", button_hover_color="#2b6218", fg_color=("#c9c9c9","#242424"))
button_debug = ctk.CTkButton(master=frame_customize, text="DEBUG", command=generate_password, fg_color="#429526")

# Frame customize checbox
frame_checkbox = ctk.CTkFrame(frame_customize, fg_color="transparent", corner_radius=10)
checkbox_customize_1 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_uppercase_tkvar, text="Uppercase", border_width=2, fg_color="#429526", hover_color="#2b6218", font=("Arial", 18))
checkbox_customize_2 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_lowercase_tkvar, text="Lowercase", border_width=2, fg_color="#429526", hover_color="#2b6218", font=("Arial", 18))
checkbox_customize_3 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_numbers_tkvar, text="Numbers", border_width=2, fg_color="#429526", hover_color="#2b6218", font=("Arial", 18))
checkbox_customize_4 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_symbols_tkvar, text="Symbols", border_width=2, fg_color="#429526", hover_color="#2b6218", font=("Arial", 18))


# ---------------------------------- Layout ---------------------------------- #
# Configure app grid
app.columnconfigure(0, weight=1, uniform="a")
app.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

# Frame password
frame_password.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
label_password.place(relx=0.02, rely=0.45, anchor="w")
progressbar_password.place(relx=0.5, rely=0.98, anchor="center")
button_password_1.pack(side="right", padx=5)
button_password_2.pack(side="right")

# Frame customize
frame_customize.grid(column=0, row=1, rowspan=5, sticky="nsew", padx=10, pady=10)
label_customize_1.place(relx=0.02, rely=0.08, anchor="w")
label_customize_2.place(relx=0.02, rely=0.40, anchor="w")
label_customize_3.place(relx=0.02, rely=0.5, anchor="w")
slider_customize.place(relx=0.06, rely=0.5, anchor="w")
#button_debug.place(relx=0.02, rely=0.9, anchor="w")

# Frame customize checbox
frame_customize.columnconfigure((0,1,3), weight=1, uniform="a")
frame_customize.rowconfigure(0, weight=1, uniform="a")
frame_checkbox.grid(column=3, row=0, sticky="nsew", padx=10, pady=10)
checkbox_customize_1.place(relx=0.4, rely=0.05, anchor="nw")
checkbox_customize_2.place(relx=0.4, rely=0.15, anchor="nw")
checkbox_customize_3.place(relx=0.4, rely=0.25, anchor="nw")
checkbox_customize_4.place(relx=0.4, rely=0.35, anchor="nw")


# ------------------------------------ Run ----------------------------------- #
# Set default theme
ChangeTheme(app).set_dark_theme()
#ChangeTheme(app).set_light_theme()

# Generate first password
generate_password()

# Run the app
app.mainloop()

# Test
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()