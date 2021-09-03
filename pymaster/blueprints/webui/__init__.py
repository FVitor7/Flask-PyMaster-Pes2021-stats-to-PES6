from flask import Blueprint, redirect, url_for

from .views import player, index



bp = Blueprint("webui", __name__, template_folder="templates")


bp.add_url_rule("/", view_func=index)
#bp.add_url_rule("/api/", view_func=redirect_api_version)
bp.add_url_rule(
    "/v1/players/<player_id>", view_func=player, endpoint="playerview"
)


def init_app(app):
    app.register_blueprint(bp)
