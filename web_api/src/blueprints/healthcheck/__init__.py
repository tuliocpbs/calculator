from flask import Blueprint

from .healthcheck import healthcheck


bp = Blueprint('Health Check Blueprint', __name__)
bp.add_url_rule('/healthcheck', view_func=healthcheck, methods=['GET'])


def init_app(app):
    app.register_blueprint(bp)
