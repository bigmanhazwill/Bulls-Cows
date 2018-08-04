import random

class Game:
    """
    Making the game
    """

    def start(self, p1, p2, code):
        """
        Begins the game ready for playing, setting up the class vars accordingly
        :param p1: The name of player 1
        :param p2: The name of player 2
        :param code: The value of the secret key
        """
        self.guess_count = 0
        self.guessed = False
        self.player_1 = p1
        self.player_2 = p2
        self.chosen_code = code

    @staticmethod
    def get_inputs():
        """
        Gathers all the user inputs for further use, also deciding whether
        1 or 2 player game
        :returns The user inputted values for player 1, 2 and the secret key
        """
        mode = int(input('2 player game, or 1 player guessing random key? (enter 1 or 2)'))
        p2 = input('Who is going to be guessing? (name) ')
        if mode == 1:
            return 'Bot', p2, str(random.randint(1000,10000))
        else:  
            p1 = input('Who is going to be creating the key? (name) ')
            code = input(p1 + ' please enter your secret key.\n')
            return p1, p2, code


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
        :returns Whether or not the guess was correct
        """
        key_guess = input(self.player_2 + ' please enter your 4 digit guess: \n')
        self.guess_count += 1

        return self.check(key_guess)

    def get_correct_position(self, guess):
        """
        Gets the amount of numbers that are in the completely right position
        :param guess: The 4 digit guess given by player 2
        :returns The number of digits in the correct position
        """
        total = 0

        for pos, num in enumerate(guess):
            if(self.chosen_code[pos] == num ):
                total += 1 
        
        return total

    def get_wrong_position(self, guess):
        """
        Gets the amount of numbers that are in the key but guessed in the wrong position
        :param guess: The 4 digit guess given by player 2
        :returns The number of digits that are in the key but guessed in wrong position
        """
        total = 0

        for pos, num in enumerate(guess):
            if(self.chosen_code[pos] != num and self.chosen_code[pos] in guess):
                total += 1 
        
        return total

    def check(self, key_guess):
        """
        Checks if current guess is right
        :param key_guess: The attempted guess at the secret key
        :returns Whether the guess was correct
        """
        if(key_guess == self.chosen_code):
            return True
        
        correct_pos = self.get_correct_position(key_guess)
        wrong_pos = self.get_wrong_position(key_guess)
        hint = '{0}-{1}'.format(correct_pos, wrong_pos) # calcs hint here as guess was incorrect

        print(hint)
        return False


if __name__ == "__main__":
    g = Game()
    p1, p2, code = g.get_inputs()
    g.start(p1, p2, code)
    while not g.guessed:
        g.guessed = g.guess()

    print('\nCongratulations {0} you guessed the key correctly in {1} guesses, it was: {2}\n'.format(g.player_2, g.guess_count, g.chosen_code) )
