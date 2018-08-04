
class Game:
    """
    Making the game
    """

    def start(self):
        """
        Begins the game ready for playing
        """
        self.guess_count = 0
        self.guessed = False
        self.player_1 = input('Who is going to be creating the key? (name) ')
        self.player_2 = input('Who is going to be guessing? (name) ')
        self.chosen_code = input(self.player_1 + ' please enter your secret key.\n')
        
        

    def __init__(self):
        """
        Setting up the initial game state.
        """
        self.chosen_code = 0000
        self.player_1 = ''
        self.player_2 = ''

    def guess(self):
        """
        Allow player 2 to perform their guess
        """
        key_guess = input(self.player_2 + ' please enter your 4 digit guess: \n')
        self.guess_count += 1
        return self.check(key_guess)

    def check(self, key_guess):
        """
        Checks if current guess is right
        """
        if(key_guess == self.chosen_code):
            return True
        
        return False


if __name__ == "__main__":
    g = Game()
    g.start()
    while not g.guessed:
        g.guessed = g.guess()
    print('\nCongratulations {0} you guessed the key correctly in {1} guesses, it was: {2}\n'.format(g.player_2, g.guess_count, g.chosen_code) )