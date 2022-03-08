import unittest
import sys

import pandas as pd 
import numpy as np

from sklearn.ensemble import RandomForestClassifier

import surge_model_training as smt


class TestSurgePriceModel(unittest.TestCase):

    def test_training_surge_classifier(self):
        
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        self.assertEqual(len(data.columns),11)
        
    
    def test_unique_values(self):
         
        data = pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        self.assertEqual(len(list(np.unique(data['surge_mult']))), 5)
        
    def test_null_values(self):
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')
        self.assertEqual(len(data), len(data.dropna()))
 
    def test_training_data(self):
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')

        feature_train = data[['temp','clouds','pressure','rain','humidity','wind','rush_hr', 'location_latitude','location_longitude']]
        target_train = data[['surge_mult']]
        self.assertEqual(len(feature_train), len(target_train))    
        
    def test_training_model(self):
        data=pd.read_csv('../feedback_app/training_testing_data/training_surge_price_classifier_df.csv')

        feature_train = data[['temp','clouds','pressure','rain','humidity','wind','rush_hr', 'location_latitude','location_longitude']]
        target_train = data[['surge_mult']]
        
        rf = RandomForestClassifier(n_estimators = 10, class_weight ='balanced')
        rf.fit(feature_train, target_train)
        
        self.assertIsNotNone(rf)
             
        
unittest.main()


