import unittest
import re


class TestGeoInfo(unittest.TestCase):
    def test_location(self):
        '''
        Tests the output(distance) of geospatial API call
        params, returns: None
        '''
        result = {'destination_addresses': ['University District, \
        Seattle, WA, USA'],
                  'origin_addresses': ['Seattle, WA 98195, USA'],
                  'rows': [{'elements': [{'distance': {'text': '0.6 km',
                                                       'value': 589},
                                          'duration': {'text': '4 mins',
                                                       'value': 214},
                                          'status': 'OK'}]}], 'status': 'OK'}
        dist_km = result['rows'][0]['elements'][0]['distance']['text']
        distance = float(re.sub(r'\D+$', '', dist_km))
        self.assertEqual(distance, 0.6)

    def test_duration(self):
        '''
        Tests the output(ETA) of geospatial API call
        params, returns: None
        '''
        result = {'destination_addresses': ['University District,\
        Seattle, WA, USA'],
                  'origin_addresses': ['Seattle, WA 98195, USA'],
                  'rows': [{'elements': [{'distance': {'text': '0.6 km',
                                                       'value': 589},
                                          'duration': {'text': '4 mins',
                                                       'value': 214},
                                          'status': 'OK'}]}], 'status': 'OK'}
        duration_min = result['rows'][0]['elements'][0]['duration']['text']
        duration = float(re.sub(r'\D+$', '', duration_min))
        self.assertEqual(duration, 4.0)
