
class Game:
    """
    Making the game
    """

    def start(self):
        """
        Begins the game ready for playing
        """
        self.player_1 = input('Who is going to be creating the key? (name) ')
        self.player_2 = input('Who is going to be guessing? (name) ')
        self.chosen_code = input(self.player_1 + ' please enter your secret key.\n')
        # TODO guess()

    def __init__(self):
        """
        Setting up the initial game state.
        """
        self.chosen_code = 0000
        self.player_1 = ''
        self.player_2 = ''


if __name__ == "__main__":
    g = Game()
    g.start()