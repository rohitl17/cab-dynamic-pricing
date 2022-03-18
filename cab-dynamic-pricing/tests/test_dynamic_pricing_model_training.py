import unittest
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score


class TestPricePredictModel(unittest.TestCase):
    '''
    Tests for the modules and models in the dynamic pricing
    training script for fedback loop
    '''
    def test_uber_traindata(self):
        '''
        Tests the training input to uber dynamic pricing training model
        params, returns: None
        '''
        uber_train = \
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
        self.assertEqual(len(uber_train.columns), 12)

    def test_lyft_traindata(self):
        '''
        Tests the training input to lyft dynamic pricing inference model
        params, returns: None
        '''
        lyft_train = \
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
        self.assertEqual(len(lyft_train.columns), 13)

    def test_uber_testdata(self):
        '''
        Tests the validation data of uber dynamic pricing inference model
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

    def test_lyft_testdata(self):
        '''
        Tests the validation data of lyft dynamic pricing inference model
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

    def test_uber_training(self):
        '''
        Tests the training module of uber dynamic pricing inference model
        params, returns: None
        '''
        uber_train = \
            pd.DataFrame({'source_lat': [42.3600825],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Black': [0], 'Black SUV': [0],
                          'UberPool': [1.0], 'UberX': [0],
                          'UberXL': [0], 'WAV': [0],
                          'uber_price': [9.0]})
        uber_test = \
            pd.DataFrame({'source_lat': [41.3000637],
                          'source_long': [-71.0588801],
                          'dest_lat': [42.3518662],
                          'dest_long': [-71.0642623],
                          'distance': [1.0],
                          'surge_multiplier': [1.0],
                          'Black': [0], 'Black SUV': [0],
                          'UberPool': [0], 'UberX': [1.0],
                          'UberXL': [0], 'WAV': [0],
                          'uber_price': [12.0]})

        xtrain = uber_train[['source_lat', 'source_long',
                             'dest_lat', 'dest_long', 'distance',
                             'surge_multiplier', 'Black', 'Black SUV',
                             'UberPool', 'UberX', 'UberXL', 'WAV']]
        ytrain = uber_train['uber_price']

        xtest = uber_test[['source_lat', 'source_long', 'dest_lat',
                           'dest_long', 'distance', 'surge_multiplier',
                           'Black', 'Black SUV', 'UberPool', 'UberX',
                           'UberXL', 'WAV']]
        ytest = uber_test['uber_price']
        uber_model = linear_model.LinearRegression()
        uber_model.fit(xtrain, ytrain)
        ypred = uber_model.predict(xtest)
        rsquared_value = r2_score(ytest, ypred)
        message = ("ERROR : test_training_model is failing")
        self.assertIsNotNone(rsquared_value, message)
