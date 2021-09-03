def amplua_encoder(amp):
    if 'GK Goalkeeper' in amp:
        return 'GK'
    if 'CB Centre Back' in amp:
        return 'CB'
    if 'RB Right Back' in amp:
        return 'RB'
    if 'LB Left Back' in amp:
        return 'LB'
    if 'DMF Defensive Midfielder' in amp:
        return 'DMF'
    if 'CMF Centre Midfielder' in amp:
        return 'CMF'
    if 'LMF Left Midfielder' in amp:
        return 'LMF'
    if 'RMF Right Midfielder' in amp:
        return 'RMF'
    if 'AMF Attacking Midfielder' in amp:
        return 'AMF'
    if 'SS Second Striker' in amp:
        return 'SS'
    if 'CF Centre Forward' in amp:
        return 'CF'
    if 'LWF Left Wing Forward' in amp:
        return 'LWF'
    if 'RWF Right Wing Forward' in amp:
        return 'RWF'
    if amp == 'Right':
        return 'R'
    if amp == 'Left':
        return 'L'
    if not amp.isdigit():
        return 'OFF'
    return amp
