import unittest
import pandas as pd


class TestUserModule(unittest.TestCase):
    '''
    Test the user creation and retrieval modules
    '''
    def test_user_database(self):
        '''
        Tests the user database for null values, datatypes
        and column entries
        params, return: None
        '''
        data = pd.read_csv('tests/test_data/users.csv')
        self.assertEqual(len(data.columns), 3)
        self.assertEqual(type(data['user_id'][0]), str)
        self.assertIsNotNone(data)
        self.assertEqual(len(data.dropna()), len(data))
