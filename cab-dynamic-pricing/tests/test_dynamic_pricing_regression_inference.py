import unittest
import sys
import pandas as pd 
import dynamic_pricing_regression_inference as dpri

class CabPricePredictor(unittest.TestCase):

    def test_get_uber_price(self):
        uber = pd.read_csv('../feedback_app/training_testing_data/uber_test_mlr.csv')

        message = "Price output is not created"
        self.assertNotEqual(uber['price'].shape, 0, message)

    def test_check_input(self):
        lyft = pd.read_csv('../feedback_app/training_testing_data/lyft_test_mlr.csv')

        message = "NaN values present in distance"
        self.assertIsNotNone(lyft['distance'], message)    

unittest.main()


