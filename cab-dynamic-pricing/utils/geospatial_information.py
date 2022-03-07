import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import json


class GeoSpacialData:
    def __init__(self, source, destination):
        """""
        
        
        """""
        self.API = ""
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
