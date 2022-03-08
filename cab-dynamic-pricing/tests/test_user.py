import unittest
import pandas as pd



class TestApp(unittest.TestCase):

    def test_training_usercsv(self):
        data=pd.read_csv('../database/users.csv')
        self.assertEqual(len(data.columns),3)
        self.assertEqual(type(data['user_id'][0]), str)
        self.assertIsNotNone(data)
        self.assertEqual(len(data.dropna()), len(data))
    




