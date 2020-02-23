import os
import json

from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/docs' # URL for exposing Swagger UI
API_URL = '' 
swagger_file_dir = os.path.abspath('./docs/api.json')
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'spec': json.load(open(swagger_file_dir))}
)
