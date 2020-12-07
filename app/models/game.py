from app.models.player import Player
class Game():


    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    def play_game(self, player1, player2):
        if self.player1.choice == "Rock" and self.player2.choice == "Paper":
            return self.player2
        elif self.player1.choice == "Rock" and self.player2.choice == "Scissors":
            return self.player1
        elif self.player1.choice == "Scissors" and self.player2.choice == "Paper":
            return self.player1
        elif self.player1.choice == self.player2.choice:
            return None

    def winner(self, player1, player2):
        result = self.play_game(player1, player2)
        if result == None:
            return "Draw"
        else:
            return f"The winner is {result}!"
        
        
