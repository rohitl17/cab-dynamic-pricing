import unittest
import pandas as pd 

class CabPricePredictor(unittest.TestCase):

    def test_check_price(self):
    	uber = pd.DataFrame({'source_lat':[42.3600825],'source_long':[-71.0588801],'dest_lat':[42.3518662],'dest_long':[-71.0642623],'distance':[1.0],'surge_multiplier':[1.0],'Black,Black SUV':[0],'UberPool':[1.0],'UberX':[0],'UberXL':[0],'WAV':[0],'uber_price':[9.0]})

    	message = "NaN values present in price"
    	self.assertIsNotNone(uber['uber_price'], message)   


    def test_check_input(self):
    	lyft = pd.DataFrame({'source_lat':[42.3600825],'source_long':[-71.0588801],'dest_lat':[42.3518662],'dest_long':[-71.0642623],'distance':[1.0],'surge_multiplier':[1.0],'Lux':[1.0],'Lux Black':[0],'Lux Black XL':[0],'Lyft':[0],'Lyft XL':[0],'Shared':[0],'lyft_price':[7.0]})

    	message = "NaN values present in distance"
    	self.assertIsNotNone(lyft['distance'], message)    
