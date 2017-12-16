from src.app_utils import APP_TITLE
from src.app_utils import GUI_STRINGS
try:
    import tkinter as tk
except ImportError:
    import Tkinter as t

class Gui:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root

        self.header_label = None
        self.word_entry = None
        self.messages_label = None
        self.messages_text = None
        self.letter_entry = None
        self.play_letter_button = None
        self.challenge_button = None
        self.new_game_button = None
        self.quit_button = None

        self.setup()

    def setup(self):
        self.root.wm_title(APP_TITLE)
        self.header_label = tk.Label(text= APP_TITLE)
        self.header_label.grid(sticky=tk.W)
        self.word_entry = tk.Entry(font="Helvetica 18 bold",
                                   state='disabled', width=35)
        self.word_entry.grid(sticky=tk.W, columnspan=3, padx=5, pady=2)
        self.messages_label = tk.Label(text= GUI_STRINGS['MESSAGE_LABEL'])
        self.messages_label.grid(sticky=tk.W, padx=5, pady=2)
        self.messages_text = tk.Text(height=10, width=50)
        self.messages_text.grid(sticky=tk.W, columnspan=4, padx=5, pady=2)
        self.letter_entry = tk.Entry(width=1)
        self.letter_entry.grid(sticky=tk.EW, padx=(5, 0), pady=2)
        self.play_letter_button = tk.Button(text=
                                            GUI_STRINGS['PLAY_LETTER_BUTTON'])
        self.play_letter_button.grid(sticky=tk.EW, row=4, column=1, pady=2)
        self.challenge_button = tk.Button(text=
                                          GUI_STRINGS['CHALLENGE_BUTTON'])
        self.challenge_button.grid(sticky=tk.EW, row=4, column=2, pady=2)

        # self.new_game_button = tk.Button(text=
        #                                     GUI_STRINGS['NEW_GAME_BUTTON'],
        #                                  relief='groove')
        # self.new_game_button.grid(row=5, column=3)
        # self.quit_button = tk.Button(text=
        #                                   GUI_STRINGS['QUIT_BUTTON'],
        #                              relief='groove')
        # self.quit_button.grid(row=5, column=4)
