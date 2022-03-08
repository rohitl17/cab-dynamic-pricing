import unittest
import sys
import pandas as pd 

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

class TestPricePredictModel(unittest.TestCase):

	def test_uber_traindata(self):
		uber_train = pd.read_csv('../feedback_app/training_testing_data/uber_train_mlr.csv')
		self.assertEqual(len(uber_train.columns),14)

	def test_lyft_traindata(self):
		lyft_train = pd.read_csv('../feedback_app/training_testing_data/lyft_train_mlr.csv')
		self.assertEqual(len(lyft_train.columns),14)

	def test_uber_testdata(self):	
		uber_test = pd.read_csv('../feedback_app/training_testing_data/uber_test_mlr.csv')
		self.assertEqual(len(uber_test.columns),14)

	def test_lyft_testdata(self):
		lyft_test = pd.read_csv('../feedback_app/training_testing_data/lyft_test_mlr.csv')
		self.assertEqual(len(lyft_test.columns),14)


	def test_uber_training(self):
		uber_train = pd.read_csv('../feedback_app/training_testing_data/uber_train_mlr.csv')
		uber_test = pd.read_csv('../feedback_app/training_testing_data/uber_test_mlr.csv')
		
		xtrain= uber_train[['source_lat','source_long', 'dest_lat', 'dest_long','distance','surge_multiplier','Black','Black SUV', 'UberPool', 'UberX', 'UberXL', 'WAV']]
		ytrain= uber_train['price']	
		xtest= uber_test[['source_lat','source_long', 'dest_lat', 'dest_long','distance','surge_multiplier','Black','Black SUV', 'UberPool', 'UberX', 'UberXL', 'WAV']]
		ytest= uber_test['price']
		
		uber_model = linear_model.LinearRegression()
		uber_model.fit(xtrain, ytrain)
		ypred = uber_model.predict(xtest)  
		rsquared_value= r2_score(ytest,ypred )
		message = ("ERROR : test_training_model is failing")
		self.assertIsNotNone(rsquared_value, message)           


unittest.main()
