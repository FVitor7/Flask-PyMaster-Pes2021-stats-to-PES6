from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from werkzeug.middleware.proxy_fix import ProxyFix
from pymaster.ext import configuration




def minimal_app(**config):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    cors = CORS(app)
    cross_origin()

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    configuration.init_app(app, **config)

    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app
