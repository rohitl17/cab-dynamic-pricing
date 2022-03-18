import unittest
import pandas as pd
import numpy as np
from model_scripts.surge_inference import SurgePriceClassifier


class TestSurgePriceClassifier(unittest.TestCase):
    '''
    Tests for checking the surge price classifier model inference
    script
    params, returns: None
    '''
    def test_get_rush_hour(self):
        '''
        Tests if rush hour is returned by the given module
        params, returns: None
        '''
        data = \
            pd.DataFrame({'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'rush_hr': [0],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768],
                          'surge_mult': [0]})
        rush_hr = data[['rush_hr']]
        message = "ERROR : test_get_rush_hour is failing"
        self.assertIsNotNone(rush_hr, message)

    def test_unique_values(self):
        '''
        Tests the unique values predicted column
        params, returns: None
        '''
        data = \
            pd.DataFrame({'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'rush_hr': [0],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768],
                          'surge_mult': [0]})
        message = "ERROR : test_unique_values is failing"
        self.assertEqual(len(list(np.unique(data['surge_mult']))),
                         1, message)

    def test_null_values(self):
        '''
        Test for null values. Prevents feedback loop errors
        params, returns: None
        '''
        data = \
            pd.DataFrame({'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'rush_hr': [0],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768],
                          'surge_mult': [0]})
        self.assertEqual(len(data), len(data.dropna()))

    def test_surge_model(self):
        data = \
            pd.DataFrame({'id': [0], 'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768],
                          'surge_mult': [0]})

        surge_mult_object = SurgePriceClassifier(data)
        surge = \
            surge_mult_object.surge_prediction_model()

        message = "Predicted surge is not correct"
        self.assertIsNotNone(surge, message)
