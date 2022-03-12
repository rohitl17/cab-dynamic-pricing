import unittest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class TestSurgePriceModel(unittest.TestCase):

    def test_training_surge_classifier(self):

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

    def test_unique_values(self):

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

        data = \
            pd.DataFrame({'temp': [40.67], 'clouds': [0.94],
                          'pressure': [1013.76], 'rain': [0.0],
                          'humidity': [0.92], 'wind': [2.92],
                          'rush_hr': [0],
                          'location_latitude': [42.3559219],
                          'location_longitude': [-71.0549768],
                          'surge_mult': [0]})
        self.assertEqual(len(data), len(data.dropna()))

    def test_training_data(self):

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
        message = "ERROR : test_training_data is failing"
        self.assertEqual(len(feature_train),
                         len(target_train), message)

    def test_training_model(self):

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
        message = ("ERROR : test_training_model is failing")
        self.assertIsNotNone(rf, message)
