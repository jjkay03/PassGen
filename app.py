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
# Widget variables
password_tkvar = tk.StringVar(value=PasswordGenerator(length=40).generate_password())
password_length_tkvar = tk.IntVar(value=15)
password_uppercase_tkvar = tk.BooleanVar(value=True)
password_lowercase_tkvar = tk.BooleanVar(value=True)
password_numbers_tkvar = tk.BooleanVar(value=True)
password_symbols_tkvar = tk.BooleanVar(value=True)

# Frame password
frame_password = ctk.CTkFrame(app, corner_radius=10)
label_password = ctk.CTkLabel(frame_password, textvariable=password_tkvar, font=("Arial", 25))
progressbar_password = ctk.CTkProgressBar(frame_password, height=10, width=785, progress_color="#00bc8c", fg_color="")
#progressbar_password.set(PasswordEvaluator(label_password_var.get()).evaluate_strength()/100)

# Frame customize
frame_customize = ctk.CTkFrame(app, corner_radius=10)
label_customize_1 = ctk.CTkLabel(frame_customize, text="Customize Password", font=("Arial Bold", 20))
label_customize_2 = ctk.CTkLabel(frame_customize, text="Password Length", font=("Arial", 18))
label_customize_3 = ctk.CTkLabel(
    master=frame_customize, 
    textvariable=password_length_tkvar,
    corner_radius=5,
    fg_color=("#c9c9c9","#242424"),
    font=("Arial", 18)
    )
slider_customize = ctk.CTkSlider(
    master=frame_customize,
    from_ = 1, to = 40,
    width=300, 
    variable=password_length_tkvar,
    progress_color="#00bc8c", 
    button_color="#008966", 
    button_hover_color="#006f53",
    fg_color=("#c9c9c9","#242424")
    )

# Frame customize checbox
frame_checkbox = ctk.CTkFrame(frame_customize, fg_color="transparent", corner_radius=10)
checkbox_customize_1 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_uppercase_tkvar, text="Uppercase", border_width=2, fg_color="#008966", hover_color="#006f53", font=("Arial", 18))
checkbox_customize_2 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_lowercase_tkvar, text="Lowercase", border_width=2, fg_color="#008966", hover_color="#006f53", font=("Arial", 18))
checkbox_customize_3 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_numbers_tkvar, text="Numbers", border_width=2, fg_color="#008966", hover_color="#006f53", font=("Arial", 18))
checkbox_customize_4 = ctk.CTkCheckBox(master=frame_checkbox, variable=password_symbols_tkvar, text="Symbols", border_width=2, fg_color="#008966", hover_color="#006f53", font=("Arial", 18))


# ---------------------------------- Layout ---------------------------------- #
# Configure app grid
app.columnconfigure(0, weight=1, uniform="a")
app.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

# Frame password
frame_password.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
label_password.place(relx=0.02, rely=0.45, anchor="w")
progressbar_password.place(relx=0.5, rely=0.98, anchor="center")

# Frame customize
frame_customize.grid(column=0, row=1, rowspan=5, sticky="nsew", padx=10, pady=10)
label_customize_1.place(relx=0.02, rely=0.08, anchor="w")
label_customize_2.place(relx=0.02, rely=0.40, anchor="w")
label_customize_3.place(relx=0.02, rely=0.5, anchor="w")
slider_customize.place(relx=0.06, rely=0.5, anchor="w")

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

# Run the app
app.mainloop()

# Test
#generated_password = PasswordGenerator(length=15).generate_password()
#password_grade = PasswordEvaluator(generated_password).evaluate_strength()