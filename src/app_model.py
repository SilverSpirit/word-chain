from app_utils import GAME_STATES
import random


class AppModel:
    def __init__(self, controller):
        self.controller = controller
        self.game_state = None
        self.word = ''

    def first_turn(self, p_choice):
        choice = p_choice
        if choice == 2:
            choice = random.choice([0, 1])

        if choice == 0:  # Human
            self.game_state = GAME_STATES['HUMAN_PLAY']
            self.controller.show_message('Your turn!')
        else:  # Computer
            self.game_state = GAME_STATES['COMPUTER_PLAY']
            self.controller.show_message("Computer's turn!")
            pass
