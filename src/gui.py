from app_utils import APP_TITLE
from app_utils import GUI_STRINGS
from app_utils import ICON

import dialog

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    import tkMessageBox as messagebox


class Gui:
    def __init__(self, controller, root):
        self.dialog_frame = tk.Frame(root)
        self.controller = controller
        self.root = root
        self.choice = None
        root.protocol('WM_DELETE_WINDOW', self.on_closing)
        img = tk.PhotoImage(data=ICON)
        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
        root.bind('<Escape>', self.on_closing)

        self.header_label = None
        self.word_entry = None
        self.messages_label = None
        self.messages_text = None
        self.letter_entry = None
        self.play_letter_button = None
        self.challenge_button = None
        self.new_game_button = None
        self.quit_button = None

        PlayerDialog(self.dialog_frame, self)

    def on_closing(self, event=None):
        self.controller.play_again = messagebox.askquestion(
            title=APP_TITLE, message='Play again?')
        self.root.destroy()

    def setup(self):
        self.root.wm_title(APP_TITLE)
        self.root.resizable(False, False)
        self.header_label = tk.Label(text=GUI_STRINGS['WORD_LABEL'])
        self.header_label.grid(sticky=tk.W)
        self.word_entry = tk.Entry(font="Helvetica 18 bold",
                                   state='disabled', width=35)
        self.word_entry.grid(sticky=tk.W, columnspan=3, padx=5, pady=2)
        self.messages_label = tk.Label(text=GUI_STRINGS['MESSAGE_LABEL'])
        self.messages_label.grid(sticky=tk.W, padx=5, pady=2)
        self.messages_text = tk.Text(height=10, width=55, state='disabled')
        self.messages_text.grid(sticky=tk.W, columnspan=4, padx=5, pady=2)
        self.letter_entry = tk.Entry(width=35)
        self.letter_entry.grid(sticky=tk.EW, padx=(5, 0), pady=2)
        self.play_letter_button = tk.Button(text=
                                            GUI_STRINGS['PLAY_LETTER_BUTTON'],
                                            command=
                                            self.controller.on_play_clicked)
        self.play_letter_button.grid(sticky=tk.EW, row=4, column=1, pady=2)
        self.challenge_button = tk.Button(text=
                                          GUI_STRINGS['CHALLENGE_BUTTON'],
                                          command=
                                          self.controller.on_challenge_clicked)
        self.challenge_button.grid(sticky=tk.EW, row=4, column=2, pady=2)

    def disable_input(self):
        self.letter_entry.config(state='disabled')
        self.challenge_button.config(state='disabled')
        self.play_letter_button.config(state='disabled')

    def enable_input(self):
        self.letter_entry.config(state='normal')
        self.challenge_button.config(state='normal')
        self.play_letter_button.config(state='normal')

        # self.new_game_button = tk.Button(text=
        #                                     GUI_STRINGS['NEW_GAME_BUTTON'],
        #                                  relief='groove')
        # self.new_game_button.grid(row=5, column=3)
        # self.quit_button = tk.Button(text=
        #                                   GUI_STRINGS['QUIT_BUTTON'],
        #                              relief='groove')
        # self.quit_button.grid(row=5, column=4)


class PlayerDialog(dialog.Dialog):
    def __init__(self, parent, game_gui):
        self.choice = tk.IntVar()
        self.root = parent
        self.game_gui = game_gui
        super().__init__(parent, title='First turn')
        self.human_check = None
        self.computer_check = None
        self.random_check = None

    def body(self, master):
        self.choice.set(2)
        self.human_check = tk.Checkbutton(master, text='Human',
                                          variable=self.choice, onvalue=0)
        self.human_check.grid(sticky=tk.W)
        self.computer_check = tk.Checkbutton(master, text='Computer',
                                             variable=self.choice, onvalue=1)
        self.computer_check.grid(sticky=tk.W)
        self.random_check = tk.Checkbutton(master, text='Random',
                                           variable=self.choice, onvalue=2)
        self.random_check.grid(sticky=tk.W)
        self.focus_force()

    def apply(self):
        self.game_gui.choice = self.choice.get()
        self.root.destroy()
        self.game_gui.setup()

    def cancel(self, event=None):
        self.root.destroy()
        self.game_gui.root.destroy()
