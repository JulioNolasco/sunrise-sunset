import requests


def event_query(lat, lng, date='today'):
    sunrise_sunset_url = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=1&date={date}'
    response = requests.get(sunrise_sunset_url)
    return response.json()
