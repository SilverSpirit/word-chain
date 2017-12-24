try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from gui import Gui

from app_model import AppModel


class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = AppModel(self)
        self.ui = Gui(self, self.root)
        if self.ui.choice != None:
            self.model.first_turn(self.ui.choice)

    def run(self):
        self.root.mainloop()

    def show_message(self, message):
        self.ui.messages_text.config(state='normal')
        self.ui.messages_text.insert(tk.END, '\n' + message)
        self.ui.messages_text.config(state='disabled')
