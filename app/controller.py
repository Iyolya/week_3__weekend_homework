from flask import render_template
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<player1>/<player2>")
def game_result():
    Game.play_game(player1, player2)
    return render_template()

