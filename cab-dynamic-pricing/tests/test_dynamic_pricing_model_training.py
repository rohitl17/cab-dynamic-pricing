import unittest
import sys
import pandas as pd 
import dynamic_pricing_model_training as dpmt


class TestPricePredictModel(unittest.TestCase):

	def test_uber_train(self):
		uber_train = pd.read_csv('./training_testing_data/uber_train_mlr.csv')
		self.assertEqual(len(uber_train.columns),14)

	def test_lyft_train(self):
		lyft_train = pd.read_csv('./training_testing_data/lyft_train_mlr.csv')
		self.assertEqual(len(lyft_train.columns),14)

	def test_uber_test(self):	
		uber_test = pd.read_csv('./training_testing_data/uber_test_mlr.csv')
		self.assertEqual(len(uber_test.columns),14)

	def test_lyft_test(self):
		lyft_test = pd.read_csv('./training_testing_data/lyft_test_mlr.csv')
		self.assertEqual(len(lyft_test.columns),14)

unittest.main()













