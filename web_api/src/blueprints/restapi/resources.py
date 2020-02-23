import http

from flask import jsonify, request
from flask_restful import Resource, Api
from schematics.exceptions import ValidationError, ModelValidationError

from src.models.models import CalculatorArgs
from src.repositories.rabbitmq import rbmq
from src.utils.logger import logger
from src.utils.api_key import authorize


class Calculator(Resource):
    decorators = [authorize]

    def post(self):
        try:
            payload = request.get_json()

            calc = CalculatorArgs(payload)
            calc.validate()

            rbmq.insert(calc)
            
            return {'status': 'ok', 'msg': 'Job inserted on queue'}, http.HTTPStatus.OK

        except (ValidationError, ModelValidationError) as e:
            logger.error(f'Error in payload validation: {repr(e)}')
            return {'status': 'error', 'msg': repr(e)}, http.HTTPStatus.BAD_REQUEST
        
        except Exception as e:
            logger.error(f'Unexpected error {repr(e)}')
            return {'status': 'error', 'msg': repr(e)}, http.HTTPStatus.INTERNAL_SERVER_ERROR
