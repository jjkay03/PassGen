# ---------------------------------------------------------------------------- #
#                             PassGen Themes Module                            #
# ---------------------------------------------------------------------------- #

import ttkbootstrap as ttk
import customtkinter as ctk


# ----------------------------- ChangeTheme Class ---------------------------- #
class ChangeTheme:
    def __init__(self, app):
        self.app = app
        self.current_theme = "dark"  # Default theme

    def toggle_theme(self):
        if self.current_theme == "light":
            self.set_dark_theme()
        elif self.current_theme == "dark":
            self.set_light_theme()

    def set_dark_theme(self):
        self.app.iconbitmap("assets/icon/icon-white.ico")  # Load icon
        ctk.set_appearance_mode("dark")  # Set ctk theme
        self.current_theme = "dark"

    def set_light_theme(self):
        self.app.iconbitmap("assets/icon/icon-black.ico")  # Load icon
        ctk.set_appearance_mode("light") # Set ctk theme
