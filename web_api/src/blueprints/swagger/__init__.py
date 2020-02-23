import os
import json

from flask import Blueprint

from .swagger import swaggerui_blueprint, SWAGGER_URL


bp = Blueprint("Swagger", __name__, url_prefix="/api")


def init_app(app):
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
