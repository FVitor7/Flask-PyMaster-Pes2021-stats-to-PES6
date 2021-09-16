from flask import abort, render_template, jsonify, request, redirect
from pymaster.models import Players
from flask_simplelogin import login_required


#@login_required
def index():
    return render_template("index.html")
    #return render_template("index.html")

#@login_required
def player(player_id):
    player = Players.query.filter_by(id=Players.PlayerID).first() or abort(
        404, "Jogador não encontrado"
    )
    return render_template("player.html", player=player)
