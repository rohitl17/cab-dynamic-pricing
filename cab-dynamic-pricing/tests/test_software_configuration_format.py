import unittest
from configuration_files import software_configuration_format as cfg


class TestSoftwareConfiguration(unittest.TestCase):
    '''
    Tests for checking the configuration file format
    '''
    def test_software_configuration(self):
        '''
        Tests the format of software configuration file
        params, returns: None
        '''
        google_oauth_credentials = {"secret_key": "",
                                    "google_client_id": '',
                                    "google_client_secret": ''}
        weather_api_credentials = {"api_key": ""}
        google_maps_api = {"api_key": ""}

        self.assertEqual(len(google_oauth_credentials.keys()), 3)
        self.assertEqual(len(weather_api_credentials.keys()), 1)
        self.assertEqual(len(google_maps_api.keys()), 1)

    def test_configuration_file(self):
        '''
        Tests the format of software configuration file
        params, returns: None
        '''
        self.assertEqual(len(cfg.google_oauth_credentials.keys()), 3)
        self.assertEqual(len(cfg.weather_api_credentials.keys()), 1)
        self.assertEqual(len(cfg.google_maps_api.keys()), 1)
        self.assertEqual(len(cfg.database_credentials), 0)
        self.assertEqual(len(cfg.lyft_api.keys()), 3)
        self.assertEqual(len(cfg.uber_api.keys()), 3)
