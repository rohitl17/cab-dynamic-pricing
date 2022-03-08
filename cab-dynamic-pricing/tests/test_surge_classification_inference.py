import unittest
import sys

import pandas as pd 
import numpy as np

#User to configure the path variable
#sys.path.append('~/cab-dynamic-pricing/cab-dynamic-pricing/model_scripts')
#import surge_classification_inference as sci

class TestSurgePriceClassifier(unittest.TestCase):

    def test_get_rush_hour(self):
        
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        rush_hr = data[['rush_hr']]
        message = "ERROR : test_get_rush_hour is failing"
        self.assertIsNotNone(rush_hr,message)
    
    def test_unique_values(self):
         
        data = pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        message = "ERROR : test_unique_values is failing"
        self.assertEqual(len(list(np.unique(data['surge_mult']))), 5, message)
    
    def test_null_values(self):
        
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        self.assertEqual(len(data), len(data.dropna()))
               
unittest.main()




