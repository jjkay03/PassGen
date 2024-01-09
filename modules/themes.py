# ---------------------------------------------------------------------------- #
#                             PassGen Themes Module                            #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk


# ----------------------------- ChangeTheme Class ---------------------------- #
class ChangeTheme:
    def __init__(self, app):
        self.app = app

    def set_dark_theme(self):
        self.app.iconbitmap("assets/icon/icon-white.ico")  # Load icon
        ctk.set_appearance_mode("dark")  # Set ctk theme
        ctk.set_default_color_theme("green")  # Set default ctk color
        ttk.Style().theme_use("darkly-ctk")  # Set the ttkbootstrap theme

    def set_light_theme(self):
        self.app.iconbitmap("assets/icon/icon-black.ico")  # Load icon
        ctk.set_appearance_mode("light") # Set ctk theme
        ctk.set_default_color_theme("green")  # Set default ctk color
        ttk.Style().theme_use("litera-ctk")  # Set the ttkbootstrap theme