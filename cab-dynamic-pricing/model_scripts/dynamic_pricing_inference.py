import pandas as pd
import pickle


class CabPricePredictor:
    def __init__(self, data_frame):
        '''
        Loading the passed dataframe and creating empty
        data frames for Uber and Lyft.
        '''
        self.data_frame = data_frame
        self.uber = pd.DataFrame()
        self.lyft = pd.DataFrame()
        self.uber_train = pd.DataFrame()
        self.lyft_train = pd.DataFrame()

    def df_modification(self):
        '''
        Splitting the columns in the dataframe into
        Uber and Lyft cab types.
        '''
        uber_list = ['Black', 'Black SUV', 'UberPool', 'UberX',
                     'UberXL', 'WAV']
        lyft_list = ['Lux', 'Lux Black', 'Lux Black XL', 'Lyft',
                     'Lyft XL', 'Shared']
        self.uber = self.data_frame[['source_lat', 'source_long',
                                     'dest_lat', 'dest_long', 'distance',
                                     'surge_multiplier', 'uber_price']]
        self.lyft = self.data_frame[['source_lat', 'source_long', 'dest_lat',
                                     'dest_long', 'distance',
                                     'surge_multiplier', 'lyft_price']]
        self.uber[['Black', 'Black SUV', 'UberPool', 'UberX', 'UberXL',
                   'WAV']] = 0
        self.lyft[['Lux', 'Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL',
                   'Shared']] = 0
        uber_type = self.data_frame["uber_cab_type"].iloc[0]
        lyft_type = self.data_frame["lyft_cab_type"].iloc[0]
        print(self.uber)
        for i in uber_list:
            if uber_type == i:
                self.uber[i] = self.uber[i].replace(0, 1)

        for i in lyft_list:
            if lyft_type == i:
                self.lyft[i] = self.lyft[i].replace(0, 1)

    def get_uber_price(self):
        """
        loading multi linear regression model for Uber to get the price.
        """
        filename = "model_weights/uber_mlr_model.sav"
        uber_mlr_model = pickle.load(open(filename, 'rb'))
        uber_price = \
            uber_mlr_model.predict(self.uber.drop(columns=['uber_price']))
        return uber_price

    def get_lyft_price(self):
        """
        loading multi linear regression model for Lyft to get the price.
        """
        filename = "model_weights/lyft_mlr_model.sav"
        lyft_mlr_model = pickle.load(open(filename, 'rb'))
        lyft_price = \
            lyft_mlr_model.predict(self.lyft.drop(columns=['lyft_price']))
        return lyft_price

    def cab_price_prediction(self):
        self.df_modification()
        uber_price = self.get_uber_price()
        lyft_price = self.get_lyft_price()
        return (round(uber_price[0], 2), round(lyft_price[0], 2))

    def df_append(self):
        """
        Appending the training datasets with the current record.
        """
        uber_ndf = pd.DataFrame()
        lyft_ndf = pd.DataFrame()
        uber_train = pd.DataFrame()
        lyft_train = pd.DataFrame()
        uber_train = \
            pd.read_csv("feedback_app/training_testing_data/\
            uber_train_mlr.csv")
        uber_ndf = pd.concat([uber_train, self.uber], axis=0)
        uber_ndf.to_csv("feedback_app/training_testing_data/\
            uber_train_mlr.csv")
        lyft_train = \
            pd.read_csv("feedback_app/training_testing_data/\
            lyft_train_mlr.csv")
        lyft_ndf = pd.concat([lyft_train, self.lyft], axis=0)
        lyft_ndf.to_csv("feedback_app/training_testing_data/\
            lyft_train_mlr.csv")
