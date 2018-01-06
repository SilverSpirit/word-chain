from app_controller import AppController


def main():
    play_game = 'yes'

    while play_game == 'yes':
        c = AppController()
        c.run()
        play_game = c.play_again


if __name__ == '__main__':
    main()
