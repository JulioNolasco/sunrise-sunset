from datetime import datetime

from app.utils.event_query import event_query


def time_until_next_event(lat, lng, type, date='today'):
    data = event_query(lat, lng, date)
    time_event = data['results'][f'{type}']
    format_time = datetime.strptime(time_event, "%I:%M:%S %p")

    current_time = datetime.strptime(datetime.now().time().strftime("%H:%M:%S"), "%H:%M:%S")
    time = (format_time - current_time).seconds

    format_time = datetime.strftime(format_time, "%H:%M:%S")
    remaing_time = "{:02}:{:02}:{:02}".format(time // 3600, (time // 60) % 60, time % 60)

    return format_time, remaing_time
