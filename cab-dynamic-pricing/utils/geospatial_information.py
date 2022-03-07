import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import json
import re
import configuration_files.software_configuration as cfg

class GeoSpatialData:
    def __init__(self, source, destination):
        """""
        
        
        """""
        self.API = cfg.google_maps_api["api_key"]
        self.source = source
        self.destination = destination
        self.geo_df = pd.DataFrame()
        
    def get_location(self):
        """""
        
        
        """""
        gmaps = googlemaps.Client(key=API)

        locationA = geolocator.geocode(self.source)
        locationB = geolocator.geocode(self.destination)
        
        self.geo_df['source_lat'] = locationA.latitude
        self.geo_df['source_long'] = locationA.longitude
        self.geo_df['dest_lat'] = locationB.latitude
        self.geo_df['dest_long'] = locationB.longitude
        
        return geo_df
    
    def get_distance(self):
        """""
        
        
        """""
        result = gmaps.distance_matrix(self.source, self.destination, mode='driving')
        dist_km = result['rows'][0]['elements'][0]['distance']['text']
        distance = float(re.sub(r'\D+$','',dist_km))
        
        return distance   
    
    def get_duration(self):
        """""
        
        
        """""
        result = gmaps.distance_matrix(self.source, self.destination, mode='driving')
        duration_mins = result['rows'][0]['elements'][0]['duration']['text']
        duration = float(re.sub(r'\D+$','',duration_mins))
        
        return duration
        
