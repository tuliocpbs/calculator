from functools import wraps
import http

from flask import jsonify, request

from src.config.api_key import ApiKeySettings
from src.utils.logger import logger


def authorize(fn):
    apikey = ApiKeySettings()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'Api-Key' not in request.headers:
            return {'status':'error', 'msg': 'Api-Key not present on Request Headers'}, http.HTTPStatus.BAD_REQUEST

        if request.headers['Api-Key'] != apikey.API_KEY:
            logger.info('Error: ApiKey not valid')
            return {'status':'error', 'msg': 'ApiKey not valid'}, http.HTTPStatus.UNAUTHORIZED

        return fn(*args, **kwargs)
    return wrapper
