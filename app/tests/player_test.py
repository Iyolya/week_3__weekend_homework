import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Laura", "Paper")
        self.player2 = Player("Luna", "Rock")

    
    def test_player_has_name(self):
        self.assertEqual("Luna", self.player2.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player2.choice)