import os

from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from flask_cors import CORS

from src.blueprints import healthcheck, swagger, restapi


app = Flask(__name__)
CORS(app)

apm = ElasticAPM(app)

healthcheck.init_app(app)
restapi.init_app(app)
