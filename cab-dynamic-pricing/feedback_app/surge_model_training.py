import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from datetime import datetime


class SurgePriceModel:
    def __init__(self):
        '''
        Loading the training dataset for the Surge Price Model and
        dividing it into features and target variables.
        '''
        self.training_dataframe = pd.read_csv('./training_testing_data/\
        training_surge_price_classifier_df.csv')
        self.testing_dataframe = pd.read_csv('./training_testing_data/\
        testing_surge_price_classifier_df.csv')
        self.feature_train = \
            self.training_dataframe[['temp', 'clouds',
                                     'pressure', 'rain', 'humidity',
                                     'wind', 'rush_hr', 'date_day',
                                     'location_latitude',
                                     'location_longitude']]
        self.target_train = \
            self.training_dataframe[['surge_mult']]
        self.feature_test = \
            self.testing_dataframe[['temp', 'clouds', 'pressure',
                                    'rain', 'humidity', 'wind', 'rush_hr',
                                    'date_day', 'location_latitude',
                                    'location_longitude']]
        self.target_test = self.testing_dataframe[['surge_mult']]
        self.result_rf_model = pd.DataFrame()

    def train_surge_classifier(self):
        '''
        Running the feature and target variables in a random forest
        classifier and appending the timestamp on the output
        '''
        rf = RandomForestClassifier(n_estimators=10,
                                    class_weight='balanced')
        rf.fit(self.feature_train, self.target_train)
        timestamp = datetime.now()
        self.result_rf_model['timestamp'] = timestamp
        filename = ('./model_dumps/surge_classification_rf_model' + timestamp)
        pickle.dump(rf, open(filename, 'wb'))
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.score(self.feature_test,
                                    self.target_test)
        self.result_rf_model['model_score'] = result
        self.result_rf_model.to_csv('./result/\
        surge_classification_rf_model' + timestamp + '.csv')
