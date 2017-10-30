try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Gui:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root

        self.header_label = None
        self.word_label = None
        self.messages_label = None
        self.messages_text = None
        self.letter_entry = None
        self.play_letter_button = None
        self.challenge_button = None
        self.new_game_button = None
        self.quit_button = None

        self.setup()

    def setup(self):
        pass