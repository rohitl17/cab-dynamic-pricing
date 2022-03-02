class SurgePriceClassifer:
    def __init__(self, data_frame):
        ''''''
        
        ''''''
        self.data_frame = data_frame
        self.predictive_surge_mapping= {1:1, 2: 1.25, 3:1.5, 4:1.75, 5:2}
    
    def get_rush_hour(self):
        ''''''
        
        ''''''
        var_hour = datetime.now().hour

        if ((var_hour >=6 & var_hour <10)|(var_hour>=15 & var_hour<19)):
            self.data_frame['rush_hour'] = [1]
        else:
            self.data_frame['rush_hour'] = [0]
    
    def surge_prediction_model(self):
        ''''''
        
        ''''''
        filename = "../model_weights/surge_classification_rf_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(self.data_frame)
        return self.predictive_surge_mapping[int(result)]
