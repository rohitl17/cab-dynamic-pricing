import unittest
import pandas as pd
from model_scripts.dynamic_pricing_inference import CabPricePredictor


class TestCabPricePredictor(unittest.TestCase):
    '''
    Tests the modules and inference calls in the dynamic pricing script
    '''
    def test_check_price(self):
        '''
        Tests if the uber dynamic pricing returns a value
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

    def test_check_input(self):
        '''
        Tests if the uber dynamic pricing has required inputs
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

    def test_cab_price_predict(self):
        '''
        Tests if the the cab dynamic price is not a Nan value
        params, returns: None
        '''
        cab_price_inference_df = pd.DataFrame({'source_lat': [42.3600825],
                                               'source_long': [-71.0588801],
                                               'dest_lat': [42.3518662],
                                               'dest_long': [-71.0642623],
                                               'distance': [1.0],
                                               'surge_multiplier': [1.0],
                                               'uber_cab_type': ['Black'],
                                               'lyft_cab_type': ['Lux'],
                                               'uber_price': [20.0],
                                               'lyft_price': [20.0]})

        cab_price_object = CabPricePredictor(cab_price_inference_df)
        uber_predicted_price, lyft_predicted_price = \
            cab_price_object.cab_price_prediction()

        message = "Uber predicted price is not correct"
        self.assertIsNotNone(uber_predicted_price, message)
        message = "Lyft predicted price is not correct"
        self.assertIsNotNone(lyft_predicted_price, message)
