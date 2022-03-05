import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

import pickle


class SurgePriceClassifer:
    def __init__(self, data_frame):
        """
        
        Loading the dataframe and coverting the commonly used
        surge price multipliers into categorical variables.
        
        """
        self.data_frame = data_frame
        self.predictive_surge_mapping= {1:1, 2: 1.25, 3:1.5, 4:1.75, 5:2}
    
    def get_rush_hour(self):
        """
        
        Based on the time of the day, a flag is assigned indicating
        if the particular hour classifies as being a rush hour or not.
        This is used as a parameter in deducing the surge price
        multiplier.
        
        """
        var_hour = datetime.now().hour

        if ((var_hour >=6 & var_hour <10)|(var_hour>=15 & var_hour<19)):
            self.data_frame['rush_hour'] = [1]
        else:
            self.data_frame['rush_hour'] = [0]
    
    def surge_prediction_model(self):
        """
        
        loading the surge price classification model using Python
        pickle load.
        
        """
        filename = "../model_weights/surge_classification_rf_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(self.data_frame)
        return self.predictive_surge_mapping[int(result)]
