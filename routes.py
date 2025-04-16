from flask import request, jsonify
from app import app

from utils import send_postback_notification


@app.route('/', methods=['GET'])
def handle_registration():
    registration_check = request.args.get('reg')
    first_deposit_check = request.args.get('ftd')
    trader_id = int(request.args.get('trader_id'))
    deposit_sum = request.args.get('sumdep')
    click_id = request.args.get('click_id')

    response_message = None

    if registration_check == 'true':
        response_message = send_postback_notification(f'reg:{click_id}:{trader_id}')
        app.logger.info(f"Успешно добавили нового пользователя с id {trader_id}")
    else:
        if first_deposit_check == 'true':
            response_message = send_postback_notification(
                f"dep:{trader_id}:{deposit_sum}")
            app.logger.info(f"Успешно установили первый депозит пользователя")
    app.logger.info(f'Request data {request.url}')
    return jsonify(response_message), 200

