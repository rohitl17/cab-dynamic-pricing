import unittest
import pandas as pd


class TestWeatherAPI(unittest.TestCase):
    '''
    Tests the Openweathermap API call module
    '''
    def test_weather_api(self):
        '''
        Tests the response of the weather API calls
        params, returns: None
        '''
        data = \
            pd.DataFrame({'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'rush_hr': [0],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768]})
        message = "ERROR : weather API is failing"
        self.assertEqual(len(data.columns), 9, message)
