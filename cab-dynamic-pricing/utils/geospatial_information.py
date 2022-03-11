import pandas as pd
from geopy.geocoders import GoogleV3
import googlemaps
import re
import configuration_files.software_configuration as cfg


class GeoSpatialData:
    def __init__(self, source, destination):
        '''
        Assigning the API key and other variables.
        '''
        self.API = cfg.google_maps_api["api_key"]
        self.source = source
        self.destination = destination
        self.geo_df = pd.DataFrame()

    def get_location(self):
        '''
        Getting the lat and long for source
        and destination.
        '''
        geolocator = GoogleV3(api_key=self.API)
        locationA = geolocator.geocode(self.source)
        locationB = geolocator.geocode(self.destination)
        self.geo_df['source_lat'] = [locationA.latitude]
        self.geo_df['source_long'] = [locationA.longitude]
        self.geo_df['dest_lat'] = [locationB.latitude]
        self.geo_df['dest_long'] = [locationB.longitude]
        return self.geo_df

    def get_distance(self):
        '''
        calculating the distance between the source
        and destination points.
        '''
        gmaps = googlemaps.Client(key=self.API)
        result = gmaps.distance_matrix(self.source,
                                       self.destination, mode='driving')
        dist_km = result['rows'][0]['elements'][0]['distance']['text']
        distance = float(re.sub(r'\D+$', '', dist_km))
        return distance

    def get_duration(self):
        '''
        calculating the Estimated Time of Arrival
        (ETA) for the cab journey between the two
        defined points.
        '''
        gmaps = googlemaps.Client(key=self.API)
        result = gmaps.distance_matrix(self.source,
                                       self.destination, mode='driving')
        duration_mins = result['rows'][0]['elements'][0]['duration']['text']
        duration = float(re.sub(r'\D+$', '', duration_mins))
        return duration
