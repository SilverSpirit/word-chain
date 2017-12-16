try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from src.gui import Gui

from src.app_model import AppModel


class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = AppModel(self)
        self.ui = Gui(self, self.root)

    def run(self):
        self.root.mainloop()