class CabPricePredictor:
    def __init__(self, data_frame):
        ''''''
        
        ''''''
        self.data_frame = data_frame
   
    def get_uber_price(self):
        ''''''
        
        ''''''
        filename = "../model_weights/uber_mlr_model.sav"
        uber_mlr_model = pickle.load(open(filename, 'rb'))
        uber_price = loaded_model.predict(self.data_frame)
        return uber_price
        
    def get_lyft_price(self):
        ''''''
        
        ''''''
        filename = "../model_weights/lyft_mlr_model.sav"
        lyft_mlr_model = pickle.load(open(filename, 'rb'))
        lyft_price = loaded_model.predict(self.data_frame)
        return lyft_price
