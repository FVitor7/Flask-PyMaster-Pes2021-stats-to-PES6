import json
from flask import jsonify
from flask_simplelogin import login_required

#@login_required
def api_home(json_player):
    jp = json.loads(json_player)
    list_api_home = []
    for data in jp:

        img_player = '/players/pes-2021/player_'\
        + str(data["PlayerID"]) + ".png"
    
        position_pes6 = data["RegisteredPosition"]
        if position_pes6 == "0":
            position_pes6 = "GK"
        elif position_pes6 == "1":
            position_pes6 = "CB"
        elif position_pes6 == "2":
            position_pes6 = "LB"
        elif position_pes6 == "3":
            position_pes6 = "RB"
        elif position_pes6 == "4":
            position_pes6 = "DMF"
        elif position_pes6 == "5":
            position_pes6 = "CMF"
        elif position_pes6 == "6":
            position_pes6 = "LMF"
        elif position_pes6 == "7":
            position_pes6 = "RMF"
        elif position_pes6 == "8":
            position_pes6 = "AMF"
        elif position_pes6 == "9":
            position_pes6 = "LWF"
        elif position_pes6 == "10":
            position_pes6 = "RWF"
        elif position_pes6 == "11":
            position_pes6 = "SS"
        elif position_pes6 == "12":
            position_pes6 = "CF"

        player_array = {"id":data["PlayerID"], "image":img_player,\
            "name":data["Name"], "age":data["Age"], "nation":data["Country"],
            "over":data["Overall"], "pos":position_pes6, "team":data["TeamName"]}
        
        list_api_home.append(player_array)
    
    
    return (jsonify(list_api_home))
