# src/models/UserModel.py
from googleplaces import GooglePlaces, types, lang 
import requests 
import json 
import geocoder
from . import API_KEY

class UserModel():

  # class constructor
  def __init__(self, data):
    pass

  def save(self):
    pass

  @staticmethod
  def get_all_users():
    #get information about ip address
    g = geocoder.ip('me') 
    # Initialising the GooglePlaces constructor 
    google_places = GooglePlaces(API_KEY) 
    
    query_result = google_places.nearby_search( 
        # lat_lng ={'lat': 46.1667, 'lng': -1.15}, 
        lat_lng ={'lat': g.latlng[0], 'lng': g.latlng[1]}, 
        radius = 1000, 
        # types =[types.TYPE_HOSPITAL] or 
        # [types.TYPE_CAFE] or [type.TYPE_BAR] 
        # or [type.TYPE_CASINO]) 
        types =[types.TYPE_PHARMACY]) 
    
    hasil = []
    for place in query_result.places: 
      hasil.append({"nama":place.name,"latitude":str(place.geo_location['lat']),"longitude":str(place.geo_location['lng'])})
      # print (place.name) 
      # print("Latitude", place.geo_location['lat']) 
      # print("Longitude", place.geo_location['lng']) 
      
    print (hasil)
    return hasil
