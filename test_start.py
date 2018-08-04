import unittest
from start import Game
 
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.game_state = Game()
 
    def test_input_name1(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.player_1, 'Harry')
 
    def test_input_name2(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.player_2, 'Paul')
 
    def test_input_code(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.chosen_code, 1234)
 
    def test_correct(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.check(1234), True)

    def test_wrong(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.check(1497), False)

    def test_faulty(self):
        self.game_state.start('Harry', 'Paul', 1234)
        self.assertEqual(self.game_state.check('Hello'), False)
 
if __name__ == '__main__':
    unittest.main()