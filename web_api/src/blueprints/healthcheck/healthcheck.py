import http
from flask import jsonify

from src.repositories.rabbitmq import rbmq
from src.utils.utils import is_open


def healthcheck():
    rbmq_health = is_open(rbmq.config.HOST, rbmq.config.PORT)

    if rbmq_health:
        return jsonify({'status': "green", 'dependencies': {"rbmq_health": rbmq_health}}), http.HTTPStatus.OK
    else:
        return jsonify({'status': "red", 'dependencies': {"rbmq_health": rbmq_health}}), http.HTTPStatus.EXPECTATION_FAILED
