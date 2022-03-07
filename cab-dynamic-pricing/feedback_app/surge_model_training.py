import numpy as np
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
from pathlib import Path  

class SurgePriceModel:
    def __init__(self):
        
        """
        
        Loading the training dataset for the Surge Price Model and
        dividing it into features and target variables.
        
        """
        
        self.training_dataframe = pd.read_csv('./training_testing_data/training_surge_price_classifier_df.csv')
        self.testing_dataframe = pd.read_csv('./training_testing_data/testing_surge_price_classifier_df.csv')
        
        self.feature_train = training_dataframe[['temp','clouds','pressure','rain','humidity','wind','rush_hr', 'date_day', 'location_latitude','location_longitude']]
        self.target_train = training_dataframe[['surge_mult']]
        self.feature_test = testing_dataframe[['temp','clouds','pressure','rain','humidity','wind','rush_hr', 'date_day', 'location_latitude','location_longitude']]
        
        
    def training_and_evaluation(self, feature_train, target_train, feature_test):
        
        """
        
        Running the feature and target variables in a random forest
        classifier and appending the timestamp on the output.
        
        """
        
        rf = RandomForestClassifier(n_estimators = 10, class_weight ='balanced')
        rf.fit(feature_train, target_train)
        
        y_pred = rf.predict(feature_test)
        
        #getting time stamp to append it into our model
        timestamp=datetime.now()
        result_rf_model['timestamp'] = timestamp
        
        filename = ('./model_dumps/surge_classification_rf_model' + timestamp)
        pickle.dump(rf, open(filename,'wb'))
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.score(feature_train, target_train)
        result_rf_model['model_score'] =result
        
        #saving the result_rf_model dataframe into results
        result_rf_model.tocsv('./result/surge_classification_rf_model' + timestamp + '.csv')
        
