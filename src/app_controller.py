try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from gui import Gui

from app_model import AppModel
import random

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = AppModel(self)
        self.ui = Gui(self, self.root)

    def run(self):
        self.root.mainloop()

    def handle_start(self, choice):
        p_choice = choice
        if p_choice == 2:
            p_choice = random.choice([0, 1])
        self.model.gameloop(p_choice)

    def show_message(self, message):
        self.ui.messages_text.config(state='normal')
        self.ui.messages_text.insert(tk.END, '\n' + message)
        self.ui.messages_text.config(state='disabled')