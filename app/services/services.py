from datetime import datetime, timedelta
from flask import jsonify
from app.config import LATITUDE_RANGE, LONGITUDE_RANGE, VALID_TYPES
from app.utils.event_query import event_query
from app.utils.next_day_event import time_until_next_event


def get_sun_info(request):
    try:
        latitude = float(request.args.get('lat'))
        longitude = float(request.args.get('lng'))
        type_param = request.args.get('type', '').lower()
    except ValueError:
        return jsonify({'error': 'Latitude, Longitude and Type must be valid values'}), 400

    if type_param not in VALID_TYPES:
        return jsonify({'error': 'Type must be "sunset" or "sunrise"'}), 400

    if not (LATITUDE_RANGE[0] <= latitude <= LATITUDE_RANGE[1]) or not (LONGITUDE_RANGE[0] <= longitude <= LONGITUDE_RANGE[1]):
        return jsonify({'error': 'Latitude and Longitude must be within valid limits'}), 400

    data = event_query(latitude, longitude)

    time_event = data['results'][f'{type_param}']

    current_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data_obj = datetime.strptime(current_timestamp, "%d-%m-%Y %H:%M:%S")

    hour_event = datetime.strptime(time_event, "%I:%M:%S %p")
    current_time = datetime.strptime(datetime.now().time().strftime("%H:%M:%S"), "%H:%M:%S")
    if hour_event.time() > current_time.time():
        exact_event_time, remaing_time = time_until_next_event(latitude, longitude, type_param)
    else:
        new_date = data_obj + timedelta(days=1)
        exact_event_time, remaing_time = time_until_next_event(latitude, longitude, type_param, date=new_date.date())
        data_obj = new_date

    response_data = {
        'remaing_time:': f'{remaing_time}',
        'exact_datetime:': f'{data_obj.date()} {exact_event_time}',
        'request_datetime:': current_timestamp
    }

    return jsonify(response_data)
