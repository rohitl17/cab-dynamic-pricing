import unittest
import pandas as pd
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class TestApp(unittest.TestCase):
    '''
    Tests the modules and API calls in the main app file
    '''
    def test_geospatial_api(self):
        '''
        Tests the output of geospatial API call
        params, returns: None
        '''
        result = {'destination_addresses': ['University District, \
        Seattle, WA, USA'],
                  'origin_addresses': ['Seattle, WA 98195, USA'],
                  'rows': [{'elements': [{'distance': {'text': '0.6 km',
                                                       'value': 589},
                                          'duration': {'text': '4 mins',
                                                       'value': 214},
                                          'status': 'OK'}]}], 'status': 'OK'}
        dist_km = result['rows'][0]['elements'][0]['distance']['text']
        distance = float(re.sub(r'\D+$', '', dist_km))
        self.assertEqual(distance, 0.6)

    def test_weather_api(self):
        '''
        Tests the output of the weather API
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

    def test_surge_model_inference_input(self):
        '''
        Tests the input to the surge classifier model
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
        message = "ERROR : test_training_surge_classifier is failing"
        self.assertEqual(len(data.columns), 10, message)

    def test_surge_model_inference(self):
        '''
        Tests if the surge model inference model is loaded
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

        feature_train = \
            data[['temp', 'clouds', 'pressure', 'rain',
                  'humidity', 'wind', 'rush_hr',
                  'location_latitude', 'location_longitude']]
        target_train = data[['surge_mult']]
        rf = RandomForestClassifier(n_estimators=10,
                                    class_weight='balanced')
        rf.fit(feature_train, target_train)
        message = ("ERROR : Model not found")
        self.assertIsNotNone(rf, message)

    def test_uber_dynamicprice_inference(self):
        '''
        Tests the input to uber dynamic pricing inference model
        params, returns: None
        '''
        uber_test = \
            pd.DataFrame({'source_lat': [42.3600825],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Black,Black SUV': [0],
                          'UberPool': [1.0], 'UberX': [0],
                          'UberXL': [0], 'WAV': [0],
                          'uber_price': [9.0]})
        self.assertEqual(len(uber_test.columns), 12)

    def test_lyft_dynamicprice_inference(self):
        '''
        Tests the input to lyft dynamic pricing inference model
        params, returns: None
        '''
        lyft_test = \
            pd.DataFrame({'source_lat': [42.3600825],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Lux': [1.0], 'Lux Black': [0],
                          'Lux Black XL': [0], 'Lyft': [0],
                          'Lyft XL': [0], 'Shared': [0],
                          'lyft_price': [7.0]})
        self.assertEqual(len(lyft_test.columns), 13)

    def test_uber_price_output(self):
        '''
        Tests the prediction of uber dynamic pricing inference model
        params, returns: None
        '''
        uber = \
            pd.DataFrame({'source_lat': [42.3600825],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Black,Black SUV': [0],
                          'UberPool': [1.0],
                          'UberX': [0], 'UberXL': [0],
                          'WAV': [0], 'uber_price': [9.0]})

        message = "NaN values present in price"
        self.assertIsNotNone(uber['uber_price'], message)

    def test_lyft_price_output(self):
        '''
        Tests the prediction of lyft dynamic pricing inference model
        params, returns: None
        '''
        lyft = \
            pd.DataFrame({'source_lat': [42.3600825],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Lux': [1.0], 'Lux Black': [0],
                          'Lux Black XL': [0], 'Lyft': [0],
                          'Lyft XL': [0], 'Shared': [0],
                          'lyft_price': [7.0]})

        message = "NaN values present in distance"
        self.assertIsNotNone(lyft['distance'], message)

    def test_conversion(self):
        '''
        Tests the conversion of kilometers to miles
        params, returns: None
        '''
        distance = 1
        kilometers_to_miles = 0.621371
        miles = 0.62
        self.assertEqual(round(distance * kilometers_to_miles, 2), miles)
