import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rock_paper_scissors import determine_winner, get_computer_choice


class TestDetermineWinner(unittest.TestCase):

    def test_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")
        self.assertEqual(determine_winner("paper", "paper"), "It's a tie!")
        self.assertEqual(determine_winner("scissors", "scissors"), "It's a tie!")

    def test_player_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
        self.assertEqual(determine_winner("paper", "rock"), "You win!")
        self.assertEqual(determine_winner("scissors", "paper"), "You win!")

    def test_computer_wins(self):
        self.assertEqual(determine_winner("rock", "paper"), "Computer wins!")
        self.assertEqual(determine_winner("paper", "scissors"), "Computer wins!")
        self.assertEqual(determine_winner("scissors", "rock"), "Computer wins!")


class TestGetComputerChoice(unittest.TestCase):

    def test_returns_valid_choice(self):
        for _ in range(50):
            choice = get_computer_choice()
            self.assertIn(choice, ["rock", "paper", "scissors"])


if __name__ == "__main__":
    unittest.main()
