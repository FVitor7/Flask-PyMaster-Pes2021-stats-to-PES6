from flask import abort, jsonify, request
from flask_restx import Resource
from flask_marshmallow import Marshmallow
import json
from pymaster.models import Nations, Players
from sqlalchemy import desc, func
from .convert_stats import convert_stats_pes2021_to_pes6
from .api_home import api_home
from flask_simplelogin import login_required

ma = Marshmallow()


class UserSchemaNation(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nations


class UserSchemaPlayer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Players


class NationResourceID(Resource):
    @login_required
    def get(self, nation_id):
        nation = Nations.query.filter_by(
            CountryID=nation_id).first() or abort(404)
        return jsonify(nation.to_dict())


class NationResource(Resource):
    @login_required
    def get(self):
        req_name = request.args.get("nation")
        if req_name == None:
            req_name = ""

        nations_find = Nations.query.filter(
            Nations.CountryName.like('%'+req_name+'%')).limit(32).all()
        user_schema = UserSchemaNation(many=True)
        output_search = user_schema.dump(nations_find)
        return jsonify(output_search)


class PlayerResourceID(Resource):
    @login_required
    def get(self, player_id):
        player = Players.query.filter_by(
            PlayerID=player_id).first() or abort(404)
        return jsonify(player.to_dict())

class PlayerResourcePes6ID(Resource):
    @login_required
    def post(self):
        posted_data = request.get_json()
        player_id = posted_data['player_id']
        player = Players.query.filter_by(
            PlayerID=player_id).first() or abort(404)
        value = player.Country
        countryToNation = Nations.query.filter_by(CountryID=value).first()
        player.Country = countryToNation.CountryName
        database = (player.to_dict())
        return convert_stats_pes2021_to_pes6(json.dumps(database))

    @login_required
    def get(self): 
        req_id = request.args.get("id")
        if req_id == None:
            req_id = 2453
        player = Players.query.filter_by(
            PlayerID=req_id).first() or abort(404)
        value = player.Country
        countryToNation = Nations.query.filter_by(CountryID=value).first()
        player.Country = countryToNation.CountryName
        database = (player.to_dict())
        return convert_stats_pes2021_to_pes6(json.dumps(database))


class PlayerHomeStats(Resource):

    @login_required
    def get(self):

        user_schemaNations = UserSchemaNation(many=True)

        req_name = request.args.get("name")
        if req_name == None:
            req_name = ""

        req_age = request.args.get("age")
        if req_age == None:
            req_age = ""

        req_team = request.args.get("team")
        if req_team == None:
            req_team = ""
        
        req_pos = request.args.get("pos")
        if req_pos == None:
            req_pos = ""
        else:
            if req_pos == 'GK':
                req_pos = "0"
            elif req_pos == 'CB':
                req_pos = "1"
            elif req_pos == 'LB':
                req_pos = "2"
            elif req_pos == 'RB':
                req_pos = "3"
            elif req_pos == 'DMF':
                req_pos = "4"
            elif req_pos == 'CMF':
                req_pos = "5"
            elif req_pos == 'LMF':
                req_pos = "6"
            elif req_pos == 'RMF':
                req_pos = "7"
            elif req_pos == 'AMF':
                req_pos = "8"
            elif req_pos == 'LWF':
                req_pos = "9"
            elif req_pos == 'RWF':
                req_pos = "10"
            elif req_pos == 'SS':
                req_pos = "11"
            elif req_pos == 'CF':
                req_pos = "12"
            
        print(req_pos)
        req_nation = request.args.get("nation")
        nation_name = ""
        if req_nation == None:
            req_nation = ""
        else:
            country_name = Nations.query.filter(Nations.CountryName.like(
                '%'+req_nation+'%')).with_entities(Nations.CountryID)
            output_Nations = user_schemaNations.dump(country_name)
            if len(output_Nations) == 0:
                nation_name = ""
            else:
                nation_name = output_Nations[0]['CountryID']
                if nation_name == 0:
                    nation_name = ""
                else:
                    nation_name = str(nation_name)

        def func_names():
            return Players.Name.like('%'+req_name+'%')
        
        def func_teams():
            return Players.TeamName.like('%'+req_team+'%')
        
        def func_nations():
            return Players.Country.like('%'+nation_name+'%')
        
        def func_positions():
            if req_pos == "":
                return Players.RegisteredPosition.like('%'+req_pos+'%')
            else:
                return Players.RegisteredPosition.like(req_pos)

        def func_age():
            if req_age == "":
                return Players.Age.like('%'+req_age+'%')
            else:
                return Players.Age.like(req_age)


        players_find = Players.query.filter(func_names(), func_teams(), \
                func_positions(), func_nations(), \
                    func_age()).order_by(desc(Players.Overall))\
                        .limit(32).all()

        for x in range(len(players_find)):
            value = (players_find[x].Country)
            countryToNation = Nations.query.filter_by(CountryID=value).first()
            players_find[x].Country = countryToNation.CountryName

        user_schema = UserSchemaPlayer(many=True)
        output_search = user_schema.dump(players_find)
        database = json.dumps(output_search)
        print(type(database))
        return api_home(database)

###############
class PlayerResource(Resource):

    @login_required
    def get(self):

        user_schemaNations = UserSchemaNation(many=True)

        req_name = request.args.get("name")
        if req_name == None:
            req_name = ""

        req_age = request.args.get("age")
        if req_age == None:
            req_age = ""

        req_team = request.args.get("team")
        if req_team == None:
            req_team = ""
        
        req_pos = request.args.get("pos")
        if req_pos == None:
            req_pos = ""
        else:
            if req_pos == 'GK':
                req_pos = "0"
            elif req_pos == 'CB':
                req_pos = "1"
            elif req_pos == 'LB':
                req_pos = "2"
            elif req_pos == 'RB':
                req_pos = "3"
            elif req_pos == 'DMF':
                req_pos = "4"
            elif req_pos == 'CMF':
                req_pos = "5"
            elif req_pos == 'LMF':
                req_pos = "6"
            elif req_pos == 'RMF':
                req_pos = "7"
            elif req_pos == 'AMF':
                req_pos = "8"
            elif req_pos == 'LWF':
                req_pos = "9"
            elif req_pos == 'RWF':
                req_pos = "10"
            elif req_pos == 'SS':
                req_pos = "11"
            elif req_pos == 'CF':
                req_pos = "12"
            
        print(req_pos)
        req_nation = request.args.get("nation")
        nation_name = ""
        if req_nation == None:
            req_nation = ""
        else:
            country_name = Nations.query.filter(Nations.CountryName.like(
                '%'+req_nation+'%')).with_entities(Nations.CountryID)
            output_Nations = user_schemaNations.dump(country_name)
            if len(output_Nations) == 0:
                nation_name = ""
            else:
                nation_name = output_Nations[0]['CountryID']
                if nation_name == 0:
                    nation_name = ""
                else:
                    nation_name = str(nation_name)

        def func_names():
            return Players.Name.like('%'+req_name+'%')
        
        def func_teams():
            return Players.TeamName.like('%'+req_team+'%')
        
        def func_nations():
            return Players.Country.like('%'+nation_name+'%')
        
        def func_positions():
            if req_pos == "":
                return Players.RegisteredPosition.like('%'+req_pos+'%')
            else:
                return Players.RegisteredPosition.like(req_pos)

        def func_age():
            if req_age == "":
                return Players.Age.like('%'+req_age+'%')
            else:
                return Players.Age.like(req_age)


        players_find = Players.query.filter(func_names(), func_teams(), \
                func_positions(), func_nations(), \
                    func_age()).order_by(desc(Players.Overall))\
                        .limit(32).all()

        for x in range(len(players_find)):
            value = (players_find[x].Country)
            countryToNation = Nations.query.filter_by(CountryID=value).first()
            players_find[x].Country = countryToNation.CountryName

        user_schema = UserSchemaPlayer(many=True)
        output_search = user_schema.dump(players_find)
        return jsonify(output_search)