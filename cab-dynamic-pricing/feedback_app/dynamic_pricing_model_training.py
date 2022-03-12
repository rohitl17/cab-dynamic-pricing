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

        Xuber_train = \
            self.uber_train[['source_lat', 'source_long', 'dest_lat',
                             'dest_long', 'distance', 'surge_multiplier',
                             'Black', 'Black SUV', 'UberPool', 'UberX',
                             'UberXL', 'WAV']]
        Yuber_train = self.uber_train['price']

        Xuber_test = \
            self.uber_test[['source_lat', 'source_long', 'dest_lat',
                            'dest_long', 'distance', 'surge_multiplier',
                            'Black', 'Black SUV', 'UberPool', 'UberX',
                            'UberXL', 'WAV']]
        Yuber_test = self.uber_test['price']

        Xlyft_train = \
            self.lyft_train[['source_lat', 'source_long', 'dest_lat',
                             'dest_long', 'distance', 'surge_multiplier',
                             'Lux', 'Lux Black', 'Lux Black XL', 'Lyft',
                             'Lyft XL', 'Shared']]
        Ylyft_train = self.lyft_train['price']

        Xlyft_test = \
            self.lyft_test[['source_lat', 'source_long', 'dest_lat',
                            'dest_long', 'distance', 'surge_multiplier',
                            'Lux', 'Lux Black', 'Lux Black XL', 'Lyft',
                            'Lyft XL', 'Shared']]
        Ylyft_test = self.lyft_test['price']

        self.result_uber = pd.DataFrame
        self.result_lyft = pd.DataFrame

    def uber_train_test(self, Xuber_train, Yuber_train,
                        Xuber_test, Yuber_test, result_uber):
        '''
        Training Uber dataset and storing the r square value.
        '''
        uber_model = linear_model.LinearRegression()
        uber_model.fit(Xuber_train, Yuber_train)

        timestamp = datetime.now()
        result_uber['timestamp'] = timestamp
        filename = ('./model_dumps/uber_mlr_model' + timestamp)
        pickle.dump(uber_model, open(filename, 'wb'))
        Yuber_pred = uber_model.predict(Xuber_test)

        rsquared_value = r2_score(Yuber_test, Yuber_pred)
        result_uber['R^2 score'] = rsquared_value

        result_uber.to_csv('./result/uber_price_mlr' + timestamp + '.csv')

    def lyft_train_test(self, Xlyft_train, Ylyft_train, Xlyft_test,
                        Ylyft_test, result_lyft):
        '''
        Training Lyft dataset and storing the r square value.
        '''
        lyft_model = linear_model.LinearRegression()
        lyft_model.fit(Xlyft_train, Ylyft_train)

        timestamp = datetime.now()
        result_lyft['timestamp'] = timestamp

        filename = ('./model_dumps/lyft_mlr_model' + timestamp)
        pickle.dump(lyft_model, open(filename, 'wb'))

        Ylyft_pred = lyft_model.predict(Xlyft_test)

        rsquared_value = r2_score(Ylyft_test, Ylyft_pred)
        result_lyft['R^2 score'] = rsquared_value
        result_lyft.to_csv('./result/lyft_price_mlr' + timestamp + '.csv')
