from sklearn import linear_model
from sklearn.metrics import r2_score
from datetime import datetime
import pickle
import pandas as pd


class PricePredictModel:
    def __init__(self):
        '''
        Reading the training datasets for Uber and Lyft and creating
        features and target variables from each of these datasets.
        '''
        self.uber_train = \
            pd.read_csv('./training_testing_data/uber_train_mlr.csv')
        self.lyft_train = \
            pd.read_csv('./training_testing_data/lyft_train_mlr.csv')

        self.uber_test = \
            pd.read_csv('./training_testing_data/uber_test_mlr.csv')
        self.lyft_test = \
            pd.read_csv('./training_testing_data/lyft_test_mlr.csv')

        self.Xuber_train = \
            self.uber_train[['source_lat', 'source_long', 'dest_lat',
                             'dest_long', 'distance', 'surge_multiplier',
                             'Black', 'Black SUV', 'UberPool', 'UberX',
                             'UberXL', 'WAV']]
        self.Yuber_train = self.uber_train['price']

        self.Xuber_test = \
            self.uber_test[['source_lat', 'source_long', 'dest_lat',
                            'dest_long', 'distance', 'surge_multiplier',
                            'Black', 'Black SUV', 'UberPool', 'UberX',
                            'UberXL', 'WAV']]
        self.Yuber_test = self.uber_test['price']

        self.Xlyft_train = \
            self.lyft_train[['source_lat', 'source_long', 'dest_lat',
                             'dest_long', 'distance', 'surge_multiplier',
                             'Lux', 'Lux Black', 'Lux Black XL', 'Lyft',
                             'Lyft XL', 'Shared']]
        self.Ylyft_train = self.lyft_train['price']

        self.Xlyft_test = \
            self.lyft_test[['source_lat', 'source_long', 'dest_lat',
                            'dest_long', 'distance', 'surge_multiplier',
                            'Lux', 'Lux Black', 'Lux Black XL', 'Lyft',
                            'Lyft XL', 'Shared']]
        self.Ylyft_test = self.lyft_test['price']

        self.result_uber = pd.DataFrame
        self.result_lyft = pd.DataFrame

    def uber_train_test(self):
        '''
        Training Uber dataset and storing the r square value.
        '''
        uber_model = linear_model.LinearRegression()
        uber_model.fit(self.Xuber_train, self.Yuber_train)

        timestamp = datetime.now()
        self.result_uber['timestamp'] = timestamp
        filename = ('./model_dumps/uber_mlr_model' + timestamp)
        pickle.dump(uber_model, open(filename, 'wb'))
        Yuber_pred = uber_model.predict(self.Xuber_test)

        rsquared_value = r2_score(self.Yuber_test, Yuber_pred)
        self.result_uber['R^2 score'] = rsquared_value

        self.result_uber.to_csv('./result/uber_price_mlr' + timestamp + '.csv')

    def lyft_train_test(self):
        '''
        Training Lyft dataset and storing the r square value.
        '''
        lyft_model = linear_model.LinearRegression()
        lyft_model.fit(self.Xlyft_train, self.Ylyft_train)

        timestamp = datetime.now()
        self.result_lyft['timestamp'] = timestamp

        filename = ('./model_dumps/lyft_mlr_model' + timestamp)
        pickle.dump(lyft_model, open(filename, 'wb'))

        Ylyft_pred = lyft_model.predict(self.Xlyft_test)

        rsquared_value = r2_score(self.Ylyft_test, Ylyft_pred)
        self.result_lyft['R^2 score'] = rsquared_value
        self.result_lyft.to_csv('./result/lyft_price_mlr' + timestamp + '.csv')
