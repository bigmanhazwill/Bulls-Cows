
class Game:
    """
    Making the game
    """

    def start(self, p1, p2, code):
        """
        Begins the game ready for playing
        """
        self.guess_count = 0
        self.guessed = False
        self.player_1 = p1
        self.player_2 = p2
        self.chosen_code = code

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

    def get_correct_position(self, guess):
        """
        Gets the amount of numbers that are in the completely right position
        """
        total = 0

        for pos, num in enumerate(guess):
            if(self.chosen_code[pos] == num ):
                total += 1 
        
        return total

    def get_wrong_position(self, guess):
        """
        Gets the amount of numbers that are in the key but guessed in the wrong position
        """
        total = 0

        for pos, num in enumerate(guess):
            if(self.chosen_code[pos] != num and self.chosen_code[pos] in guess):
                total += 1 
        
        return total

    def check(self, key_guess):
        """
        Checks if current guess is right
        """
        if(key_guess == self.chosen_code):
            return True
        
        correct_pos = self.get_correct_position(key_guess)
        wrong_pos = self.get_wrong_position(key_guess)
        print('{0}-{1}'.format(correct_pos, wrong_pos))
        return False


if __name__ == "__main__":
    g = Game()
    p1 = input('Who is going to be creating the key? (name) ')
    p2 = input('Who is going to be guessing? (name) ')
    code = input(p1 + ' please enter your secret key.\n')
    g.start(p1, p2, code)

    while not g.guessed:
        g.guessed = g.guess()

    print('\nCongratulations {0} you guessed the key correctly in {1} guesses, it was: {2}\n'.format(g.player_2, g.guess_count, g.chosen_code) )
