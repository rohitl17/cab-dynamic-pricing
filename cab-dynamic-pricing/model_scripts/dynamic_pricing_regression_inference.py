import pandas as pd

class CabPricePredictor:
    def __init__(self, data_frame):
        """
        
        Loading the passed dataframe and creating empty data frames for 
        Uber and Lyft.
        
        """
        self.data_frame = data_frame
        self.uber = pd.DataFrame()
        self.lyft = pd.DataFrame()
        self.uber_train = pd.DataFrame()
        self.lyft_train = pd.DataFrame()
        
    def df_modification(self):   
        """
        
        Splitting the columns in the dataframe into Uber and Lyft cab types.
        
        """
        uber_list = ['Black','Black SUV', 'UberPool', 'UberX', 'UberXL', 'WAV']
        lyft_list = ['Lux','Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL', 'Shared']
        
        self.uber = self.data_frame[['source_lat','source_long', 'dest_lat', 'dest_long','distance','surge_multiplier']]
        self.lyft = self.data_frame[['source_lat','source_long', 'dest_lat', 'dest_long','distance','surge_multiplier']]
        
        self.uber[['Black','Black SUV', 'UberPool', 'UberX', 'UberXL', 'WAV']] = 0
        self.lyft[['Lux','Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL', 'Shared']] = 0
        
        uber_type = self.data_frame["uber_type"].iloc[0]
        lyft_type = self.data_frame["lyft_type"].iloc[0]
        
        for i in uber_list:
            if uber_type==i:
                self.uber[i]=self.uber[i].replace(0,1)
                
        for i in lyft_list:
            if lyft_type==i:
                self.lyft[i]=self.lyft[i].replace(0,1)
        
        
    def get_uber_price(self):
        """
        
        loading multi linear regression model for Uber to get the price.
        
        """
        filename = "../model_weights/uber_mlr_model.sav"
        uber_mlr_model = pickle.load(open(filename, 'rb'))
        uber_price = loaded_model.predict(self.uber)
        return uber_price
        
    def get_lyft_price(self):
        """
        
        loading multi linear regression model for Lyft to get the price.
        
        """
        filename = "../model_weights/lyft_mlr_model.sav"
        lyft_mlr_model = pickle.load(open(filename, 'rb'))
        lyft_price = loaded_model.predict(self.lyft)
        return lyft_price

    def df_append(self):
        """
        
        
        """
        uber_ndf = pd.DataFrame()
        lyft_ndf = pd.DataFrame()
        uber_train = pd.DataFrame()
        lyft_train = pd.DataFrame()
        
        uber_train =  pd.read_csv("../feedback_app/training_testing_data/uber_train_mlr.csv")
        uber_ndf = pd.concat([uber_train, self.uber], axis=0)
        uber_ndf.to_csv("../feedback_app/training_testing_data/uber_train_mlr.csv")
        
        lyft_train =  pd.read_csv("../feedback_app/training_testing_data/lyft_train_mlr.csv")
        lyft_ndf = pd.concat([lyft_train, self.lyft], axis=0)
        lyft_ndf.to_csv("../feedback_app/training_testing_data/lyft_train_mlr.csv")
        
