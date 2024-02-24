from flask import Blueprint
from app.controllers import get_sun_info_get as get_sun_info

sun_info_routes = Blueprint('sun_info', __name__)


@sun_info_routes.route('/api/sun-info-get', methods=['GET'])
def get_sun_info_get():
    return get_sun_info()
