from flask import Blueprint
from flask_restx import Api, fields

from .resources import PlayerResourcePes6ID, PlayerHomeStats, NationResourceID, NationResource, PlayerResourceID, PlayerResource

bp = Blueprint("restapi", __name__, url_prefix="/api/")


api = Api(bp, doc='/', version='1.0', title='PesMaster Database API',
    description="Uma API com o banco de dados do PES2021 convertido para PES6\n\nDesenvolvido por: Fábio Vitor \n\nGithub: https://github.com/FVitor7\nemail: fabvitor2010@gmail.com\n\nPara acessar a api vá para a url: http://localhost:5000/api/v1/")


ns = api.namespace("nations", description="API  operations")

nations = api.model('API', {
    "CountryID": fields.Integer(readonly=True, description='Necessário para identificar o jogador'),
    "CountryName": fields.String(required=True, description='URL da imagem do jogador'),
    "Region": fields.Integer(required=True, description='Necessário para identificar o jogador'),
    "Continent": fields.Integer(required=True, description='Necessário para identificar o jogador'),
})



def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(PlayerHomeStats, "v1/")
    api.add_resource(PlayerResource, "v1/players/")
    api.add_resource(PlayerResourcePes6ID, "v1/players/pes6/")
    api.add_resource(PlayerResourceID, "v1/players/<player_id>")
    api.add_resource(NationResource, "v1/nations/")
    api.add_resource(NationResourceID, "v1/nations/<nation_id>")
    
    
