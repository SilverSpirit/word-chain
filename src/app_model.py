from app_utils import GAME_STATES
from app_utils import WORD_LIST
from app_utils import CHALLENGE_CODE
import random


class AppModel:
    def __init__(self, controller):
        self.controller = controller
        self.game_state = None
        self.word = ''
        self.word_list = WORD_LIST[:]  # copy
        self.comp_player = ComputerPlayer()
        self.protocol = [CHALLENGE_CODE]

    def play_turn(self, p_choice):
        turn = p_choice
        if turn == 2:
            turn = random.choice([0, 1])

        if turn == 0:  # Human
            self.game_state = GAME_STATES['HUMAN_PLAY']
            self.controller.show_message('Your turn...')
        else:  # Computer
            self.game_state = GAME_STATES['COMPUTER_PLAY']
            self.controller.show_message("Computer's turn...")
            move = self.comp_player.get_action(self.word, self.word_list)
            if move not in self.protocol:
                self.word += move
                self.controller.reshow_word(self.word)
                self.controller.show_message('Computer plays {}'.format(move))
                self.update_wordlist()
                self.game_state = GAME_STATES['HUMAN_PLAY']
                self.controller.show_message('Your turn...')
            else:
                if move == CHALLENGE_CODE:
                    self.controller.show_message(
                        'Computer challenges you! Type in the full '
                        'word and hit play!')
                    self.game_state = GAME_STATES['HUMAN_CHALLENGED']

    def challenge_computer(self):
        self.controller.show_message('You challenge the computer!')
        return self.comp_player.get_action(CHALLENGE_CODE, self.word_list)
        # game over here

    def update_wordlist(self):
        self.word_list = [wrd for wrd in self.word_list if wrd[:len(
            self.word)] == self.word]



class ComputerPlayer:  # separate for convenience
    def __init__(self):
        pass  # nothing for now

    def get_action(self, word, word_list):
        # will never complete a word!
        # to add: bluffing
        if word == '':
            return random.choice(word_list)[0].upper()

        if word == CHALLENGE_CODE:
            if len(word_list) > 0:
                return random.choice(word_list)
            else:
                return ''

        # roll a dice to challenge straight off
        upper_lim = len(word_list)
        if upper_lim < 2:
            upper_lim = 2
        dice_roll = random.choice(range(1, upper_lim))
        to_challenge = dice_roll == 1
        if to_challenge:
            return CHALLENGE_CODE

        # else return a letter from the existing words or challenge
        sub_list = [wrd for wrd in word_list if len(wrd) > len(word) + 1]
        if sub_list == []:
            return CHALLENGE_CODE  # won't complete, challenge instead
        else:
            return random.choice(sub_list)[len(word)]
