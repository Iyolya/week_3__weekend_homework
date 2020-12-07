# from game_class import Game
from player import Player

class Game:

    player1 = Player("Scooby Doo", "Paper")
    player2 = Player("Shaggy", "Rock")
    player3 = Player("Velma", "Scissors")
# players = [player1, player2, player3]
# game = Game(player1, player2)



    def play_game(player1, player2):
        if player1.choice == "Rock" and player2.choice == "Paper":
            return f"{player2} won by playing {player2.choice}!"
        elif player1.choice == "Rock" and player2.choice == "Scissors":
            return f"{player1} won by playing {player1.choice}!"
        elif player1.choice == "Scissors" and player2.choice == "Paper":
            return f"{player1} won by playing {player1.choice}!"
        elif player1.choice == player2.choice:
            return None
        

    # def winner(self, player1, player2):
    #     result = play_game(self.game.player1, player2)
    #     if result == None:
    #         return "It's Draw!"
    #     else:
    #         return f"The winner is {result}!"
        
