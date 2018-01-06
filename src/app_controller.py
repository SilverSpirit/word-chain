try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from gui import Gui

from app_model import AppModel
from app_utils import GAME_STATES


class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = AppModel(self)
        self.ui = Gui(self, self.root)
        self.play_again = 'no'
        if self.ui.choice != None:
            self.model.play_turn(self.ui.choice)

    def run(self):
        self.root.mainloop()

    def show_message(self, message):
        self.ui.messages_text.config(state='normal')
        self.ui.messages_text.insert(tk.END, '\n' + message)
        self.ui.messages_text.config(state='disabled')
        self.ui.messages_text.see('end')

    def reshow_word(self, word):
        self.ui.word_entry.config(state='normal')
        self.ui.word_entry.delete(0, tk.END)
        self.ui.word_entry.insert(0, word)
        self.ui.word_entry.config(state='disabled')


    def on_play_clicked(self):
        if self.model.game_state == GAME_STATES['HUMAN_PLAY']:
            move = self.ui.letter_entry.get()
            if move == '' or not move[0].isalpha():
                self.show_message('Please enter a valid letter')
            else:
                move = move[0].upper()
                self.model.word += move
                self.reshow_word(self.model.word)
                self.show_message('You play {}'.format(move))
                if self.model.word in self.model.word_list:
                    self.model.state = GAME_STATES['COMPUTER_WIN']
                    self.show_message('Whoops! You completed a word! ({})'
                        .format(self.model.word))
                    self.show_message('Computer wins!')
                    self.ui.disable_input()
                    return
                self.model.update_wordlist()
                self.game_state = GAME_STATES['COMPUTER_PLAY']
                self.model.play_turn(1)

        elif self.model.game_state == GAME_STATES['HUMAN_CHALLENGED']:
            move = self.ui.letter_entry.get().upper()
            if move in self.model.word_list:
                self.model.state = GAME_STATES['HUMAN_WIN']
                self.show_message('You respond with {}'.format(
                    move))
                self.show_message('You win!')
                self.ui.disable_input()
            else:
                self.model.state = GAME_STATES['COMPUTER_WIN']
                self.show_message('Whoops! {} is not a valid word'.format(
                    move))
                self.show_message('Computer wins!')
                self.ui.disable_input()
        self.ui.letter_entry.delete(0, 'end')

    def on_challenge_clicked(self):
        if self.model.game_state == GAME_STATES['HUMAN_PLAY']:
            self.model.game_state = GAME_STATES['COMPUTER_CHALLENGED']
            move = self.model.challenge_computer()
            if move != '':
                self.model.state = GAME_STATES['COMPUTER_WIN']
                self.show_message('Computer responds with {}'.format(
                    move))
                self.show_message('Computer wins!')
            else:
                self.model.state = GAME_STATES['HUMAN_WIN_WIN']
                self.show_message('Computer fails to come up with a '
                                  'word')
                self.show_message('You win!')
            self.ui.disable_input()
