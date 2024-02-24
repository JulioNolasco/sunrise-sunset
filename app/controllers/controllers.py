from flask import jsonify, request
from app.services import get_sun_info


def get_sun_info_get():
    try:
        return get_sun_info(request)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
