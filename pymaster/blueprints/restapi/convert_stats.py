import json
from flask import jsonify
from .amplua import amplua_encoder


def convert_stats_pes2021_to_pes6(json_player):
    jp = json.loads(json_player)
    hab_value = 2
    ataque_pes6 = int(jp["OffensiveAwareness"]) + hab_value
    if ataque_pes6 > 99:
        ataque_pes6 = 99

    defesa_pes6 = int(round((jp["DefensiveAwareness"] +
                             jp["BallWinning"] + jp["Aggression"]) / 3)) + hab_value
    if defesa_pes6 > 99:
        defesa_pes6 = 99

    balance_pes6 = int(round((jp["Balance"] + jp["TightPossession"]
                              + jp["PhysicalContact"]) / 3)) + hab_value
    if balance_pes6 > 99:
        balance_pes6 = 99

    stamina_pes6 = int(jp["Stamina"]) + hab_value
    if stamina_pes6 > 99:
        stamina_pes6 = 99

    speed_pes6 = int(jp["Speed"]) + hab_value
    if speed_pes6 > 99:
        speed_pes6 = 99

    acc_pes6 = int(jp["Acceleration"]) + hab_value
    if acc_pes6 > 99:
        acc_pes6 = 99

    position_pes6 = jp["RegisteredPosition"]
    if position_pes6 == 0:
        position_pes6 = "GK"
    elif position_pes6 == 1:
        position_pes6 = "CB"
    elif position_pes6 == 2:
        position_pes6 = "LB"
    elif position_pes6 == 3:
        position_pes6 = "RB"
    elif position_pes6 == 4:
        position_pes6 = "DMF"
    elif position_pes6 == 5:
        position_pes6 = "CMF"
    elif position_pes6 == 6:
        position_pes6 = "LMF"
    elif position_pes6 == 7:
        position_pes6 = "RMF"
    elif position_pes6 == 8:
        position_pes6 = "AMF"
    elif position_pes6 == 9:
        position_pes6 = "LWF"
    elif position_pes6 == 10:
        position_pes6 = "RWF"
    elif position_pes6 == 11:
        position_pes6 = "SS"
    elif position_pes6 == 12:
        position_pes6 = "CF"

    positions_delanteros_pes6 = ["LWF", "SS", "CF", "RWF", "LMF", "AMF", "RMF"]
    positions_defences_pes6 = ["DMF", "CMF", "LB", "CB", "RB", "GK"]

    if position_pes6 in positions_delanteros_pes6:
        response_pes6 = int(round(ataque_pes6 + acc_pes6 +
                                  int(jp["BallControl"])) / 3) + hab_value
    else:
        response_pes6 = int(round((jp["BallWinning"] +
                                   jp["Aggression"]) / 2)) + hab_value

    if response_pes6 > 99:
        response_pes6 = 99

    agility_pes6 = int(jp["TightPossession"]) + hab_value
    if agility_pes6 > 99:
        agility_pes6 = 99

    dribble_acc_pes6 = int(jp["Dribbling"]) + hab_value
    if dribble_acc_pes6 > 99:
        dribble_acc_pes6 = 99

    dribble_spd_pes6 = int(
        round((dribble_acc_pes6 + speed_pes6) / 2)) + hab_value
    if dribble_spd_pes6 > 99:
        dribble_spd_pes6 = 99

    spa_pes6 = int(jp["LowPass"]) + hab_value
    if spa_pes6 > 99:
        spa_pes6 = 99

    sps_pes6 = int(round((spa_pes6 + int(jp["KickingPower"]))/2)) + hab_value
    if sps_pes6 > 99:
        sps_pes6 = 99

    lpa_pes6 = int(jp["LoftedPass"]) + hab_value
    if lpa_pes6 > 99:
        lpa_pes6 = 99

    lps_pes6 = int(round(int(jp["LoftedPass"]) +
                         int(jp["KickingPower"]))/2) + hab_value
    if lps_pes6 > 99:
        lps_pes6 = 99

    shot_acc_pes6 = int(jp["Finishing"]) + hab_value
    if shot_acc_pes6 > 99:
        shot_acc_pes6 = 99

    shot_power_pes6 = int(jp["KickingPower"]) + hab_value
    if shot_power_pes6 > 99:
        shot_power_pes6 = 99

    shot_tec_pes6 = int(round(shot_acc_pes6 + int(jp["Balance"]) +
                              int(jp["PhysicalContact"]) +
                              (jp["OffensiveAwareness"])) / 4) + hab_value
    if shot_tec_pes6 > 99:
        shot_tec_pes6 = 99

    fkk_pes6 = int(jp["PlaceKicking"]) + hab_value
    if fkk_pes6 > 99:
        fkk_pes6 = 99

    swerve_pes6 = int(jp["Curl"]) + hab_value
    if swerve_pes6 > 99:
        swerve_pes6 = 99

    heading_pes6 = int(jp["Heading"]) + hab_value
    if heading_pes6 > 99:
        heading_pes6 = 99

    jump_pes6 = int(jp["Jump"]) + hab_value
    if jump_pes6 > 99:
        jump_pes6 = 99

    tec_pes6 = int(round(int(jp["BallControl"]) +
                         shot_tec_pes6) / 2) + hab_value
    if tec_pes6 > 99:
        tec_pes6 = 99

    agression_pes6 = int(jp["OffensiveAwareness"]) + hab_value
    if agression_pes6 > 99:
        agression_pes6 = 99

    mentality_pes6 = int(round(int(jp["OffensiveAwareness"]) +
                               int(jp["Aggression"]))/2) + hab_value
    if mentality_pes6 > 99:
        mentality_pes6 = 99

    gk_pes6 = int(jp["GKAwareness"]) + hab_value
    if gk_pes6 > 99:
        gk_pes6 = 99

    team_work_pes6 = int(round(ataque_pes6+defesa_pes6 +
                               spa_pes6+lpa_pes6)/4) + hab_value
    if team_work_pes6 > 99:
        team_work_pes6 = 99

    wfa_pes6 = int(jp["WeakFootAccuracy"])
    wfa_pes6 = wfa_pes6 * 2
    if shot_tec_pes6 < 85:
        wfa_pes6 - 1

    wff_pes6 = int(jp["WeakFootUsage"])
    wff_pes6 = wff_pes6 * 2
    if shot_tec_pes6 < 88:
        wff_pes6 - 1

    age_pes6 = int(jp["Age"])
    consistency_pes6 = 3
    if age_pes6 < 21:
        if stamina_pes6 < 75:
            consistency_pes6 = 5
        if stamina_pes6 > 75:
            consistency_pes6 = 6
        if stamina_pes6 > 85:
            consistency_pes6 = 7
        if stamina_pes6 > 90:
            consistency_pes6 = 8

    if age_pes6 < 30 and age_pes6 > 22:
        if stamina_pes6 < 70:
            consistency_pes6 = 2
        if stamina_pes6 > 75:
            consistency_pes6 = 3
        if stamina_pes6 > 75:
            consistency_pes6 = 4
        if stamina_pes6 > 80:
            consistency_pes6 = 5
        if stamina_pes6 > 85:
            consistency_pes6 = 6
        if stamina_pes6 > 90:
            consistency_pes6 = 7
        if stamina_pes6 > 95:
            consistency_pes6 = 8

    if age_pes6 > 30:
        if stamina_pes6 < 70:
            consistency_pes6 = 1
        if stamina_pes6 > 75:
            consistency_pes6 = 2
        if stamina_pes6 > 75:
            consistency_pes6 = 3
        if stamina_pes6 > 80:
            consistency_pes6 = 4
        if stamina_pes6 > 85:
            consistency_pes6 = 5
        if stamina_pes6 > 90:
            consistency_pes6 = 6
        if stamina_pes6 > 95:
            consistency_pes6 = 7

    condition_pes6 = int(jp["Form"])

    injury_pes6 = int(jp["InjuryResistance"])
    if injury_pes6 == 3:
        injury_pes6 = 'A'
    if injury_pes6 == 2:
        injury_pes6 = 'B'
    if injury_pes6 == 1:
        injury_pes6 = 'C'

    special_alibities_pes6 = []

    if (jp['Trickster'] == 1) or (jp['MazingRun'] == 1):
        special_alibities_pes6.append('Dribbling')

    if jp['Gamesmanship'] == 1:
        special_alibities_pes6.append('Tactical Dribble')

    if (jp['PlayingStyles'] == 1) or (jp['PlayingStyles'] == 6):
        special_alibities_pes6.append('Positioning')

    if agility_pes6 > 90:
        special_alibities_pes6.append('Reaction')

    if jp['Captaincy'] == 1:
        if position_pes6 == 'GK':
            pass
        else:
            special_alibities_pes6.append('Playmaking')

    if spa_pes6 > 90 or lpa_pes6 > 90:
        special_alibities_pes6.append('Passing')

    if jp["PlayingStyles"] == 3:
        special_alibities_pes6.append('Scoring')

    if shot_tec_pes6 > 90 or shot_acc_pes6 > 90:
        special_alibities_pes6.append('1-1 Scoring')

    if jp["PlayingStyles"] == 8:
        special_alibities_pes6.append('Post Player')

    if jp["SpeedingBullet"] == 1:
        special_alibities_pes6.append('Lines')

    if (jp['LongRanger'] == 1) or (jp['LongRangeShooting'] == 1):
        special_alibities_pes6.append('Middle Shooting')

    if (jp["PlayingStyles"] == 4) or (jp["PlayingStyles"] == 21) or \
        (jp["PlayingStyles"] == 15) or (jp["PlayingStyles"] == 12) :
        special_alibities_pes6.append('Side')

    if (jp["PlayingStyles"] == 5)  or (jp["PlayingStyles"] == 14)  \
        or (jp["PlayingStyles"] == 7)  or (jp["PlayingStyles"] == 20) \
            or (jp["PlayingStyles"] == 6) or (jp["PlayingStyles"] == 8):
        special_alibities_pes6.append('Centre')

    if jp["PenaltySpecialist"] == 1:
        special_alibities_pes6.append('Penalties')

    if jp["OneTouchPass"]:
        special_alibities_pes6.append('1-Touch Pass')

    if jp["KnuckleShot"]:
        special_alibities_pes6.append('Outside')

    if (jp["PlayingStyles"] == 9) or (jp["ManMarking"] == 1):
        special_alibities_pes6.append('Marking')

    if (jp["PlayingStyles"] == 9) or (jp["PlayingStyles"] == 12) or\
        (jp["PlayingStyles"] == 8):
        special_alibities_pes6.append('Covering')

    if jp["Interception"]:
        special_alibities_pes6.append('Sliding')

    if jp["Captaincy"]:
        if position_pes6 == 'GK':
            pass
        else:
            special_alibities_pes6.append('D-Line Control')

    if jp["GKPenaltySaver"] == 1:
        special_alibities_pes6.append('Penalty Stopper')

    if (jp["PlayingStyles"] == 17):
        special_alibities_pes6.append('1-On-1 Stopper')

    if jp["GKLongThrow"]:
        special_alibities_pes6.append('Long Throw')

    if jp["Captaincy"]:
        team_work_pes6 = team_work_pes6 + 5
    #print(spec_pes6_1, spec_pes6_2, spec_pes6_3)

    positions_in_pesmaster = []
    if (jp['RWF'] == 1) or jp['LWF'] == 1:
        positions_in_pesmaster.append('WF')
    
    if jp['RMF'] == 1 or jp['LMF'] == 1:
        positions_in_pesmaster.append('SMF')

    if position_pes6 == 'LWF' or position_pes6 == 'RWF':
         position_pes6 = 'WF'
    if (position_pes6 == 'RMF') or (position_pes6 == 'LMF'):
         position_pes6 = 'SMF'

    #position_in_pesmaster = positions_in_pesmaster[position_pes6]
 
    if position_pes6 == 'GK':
        defesa_pes6 = int(jp["GKAwareness"])
        response_pes6 = int(jp["Overall"]) - hab_value
        agility_pes6 = int(jp["GKReflexes"])

    positions_ps2=[]
    if (jp["GK"] == 1) or (jp["GK"] == 2):
        positions_ps2.append("GK")
    if (jp["CB"] == 1) or (jp["CB"] == 2):
        positions_ps2.append("SB")
    if (jp["LB"] == 1) or (jp["LB"] == 2):
        positions_ps2.append("SB")
    if (jp["DMF"] == 1):
        positions_ps2.append("DMF")
    if (jp["LMF"] == 1) or (jp["LMF"] == 2):
        positions_ps2.append("SMF")
    if (jp["RMF"] == 1) or (jp["RMF"] == 2):
        positions_ps2.append("SMF")
    if (jp["AMF"] == 1) or (jp["AMF"] == 2):
        positions_ps2.append("AMF")
    if (jp["LWF"] == 1) or (jp["LWF"] == 2):
        positions_ps2.append("WF")
    if (jp["RWF"] == 1) or (jp["RWF"] == 2):
        positions_ps2.append("WF")
    if (jp["SS"] == 1) or (jp["SS"] == 2):
        positions_ps2.append("SS")
    if (jp["CF"] == 1) or (jp["CF"] == 2):
        positions_ps2.append("CF")
    
    positions_ps2 = list(dict.fromkeys(positions_ps2))
    positions_ps2 = ','.join([str(elem) for elem in positions_ps2]) 

    
    special_alibities_pes6 = ','.join([str(elem) for elem in special_alibities_pes6])

    if jp["StrongerFoot"] == 0:
        foot = "R"
    else:
        foot = "L"
    
    img_player = "https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_" + str(jp["PlayerID"]) +  ".png"

    player_array = {"id":jp["PlayerID"],"positions":positions_ps2,\
        "special_abilities":special_alibities_pes6,"img_player":img_player,\
            "Age":jp["Age"], "team":jp["TeamName"], "nation":jp["Country"],
        "Stronger_Foot":foot, "Height":jp["Height"], "Weight": jp["Weight"],
            "name":jp["Name"], "Position":position_pes6,"attack":ataque_pes6,"defence":defesa_pes6,"balance":balance_pes6,\
        "stamina":stamina_pes6,"speed":speed_pes6,"acceleration":acc_pes6,"response":response_pes6,\
            "agility":agility_pes6,"dribble_accuracy":dribble_acc_pes6,"dribble_speed":dribble_spd_pes6,\
                "short_pass_accuracy":spa_pes6,"long_pass_speed":sps_pes6,"long_pass_accuracy":lpa_pes6,\
                    "short_pass_speed":lps_pes6,"shot_accuracy":shot_acc_pes6,"shot_power":shot_power_pes6,\
                    "shot_technique":shot_tec_pes6,"free_kick_accuracy":fkk_pes6,"swerve":swerve_pes6,\
                        "heading":heading_pes6,"jump":jump_pes6,"technique":tec_pes6,\
                            "aggression":agression_pes6,"mentality":mentality_pes6,"gk_skills":gk_pes6,\
                                "team_work":team_work_pes6,"consistency":consistency_pes6,\
                                    "condition":condition_pes6,"weak_foot_accuracy":wfa_pes6,\
                                        "weak_foot_frequency":wff_pes6,
                                        "free_kick_style":1,"drop_kick_style":1,"dribbling_style":1,
                                        "penalty_style":1,"injury":injury_pes6}

    
    
    return (jsonify(player_array))
    
