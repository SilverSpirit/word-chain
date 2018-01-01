from app_controller import AppController


def main():
    play_game = True

    while play_game:
        c = AppController()
        c.run()
        play_game = c.play_again


if __name__ == '__main__':
    main()
