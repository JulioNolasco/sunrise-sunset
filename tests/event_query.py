from unittest.mock import patch
import unittest
from requests_mock import Mocker
from app.utils.event_query import event_query


class TestEventQuery(unittest.TestCase):

    @patch('requests.get')
    def test_event_query(self, mock_get):
        lat = 40.7128
        lng = -74.0060
        date = '2024-02-24'

        mock_response = {
            'results': {
                'sunrise': '6:30:00 AM',
                'sunset': '6:00:00 PM',
            }
        }

        mock_get.return_value.json.return_value = mock_response

        result = event_query(lat, lng, date)

        expected_result = mock_response
        self.assertEqual(result, expected_result)

        expected_url = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=1&date={date}'
        mock_get.assert_called_once_with(expected_url)


class TestEventQueryIntegration(unittest.TestCase):

    def test_event_query_integration(self):
        with Mocker() as mocker:
            # Mock da resposta da API
            expected_response = {
                'results': {
                    'sunrise': '07:00:00 AM',
                    'sunset': '06:00:00 PM'
                }
            }
            mocker.get('https://api.sunrise-sunset.org/json?lat=0&lng=0&formatted=1&date=today', json=expected_response)

            # Chama a função event_query
            result = event_query(0, 0)

            # Assert para verificar se a resposta é a esperada
            self.assertEqual(result, expected_response)


if __name__ == '__main__':
    unittest.main()
