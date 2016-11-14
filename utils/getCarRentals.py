import amadeus
import requests
import pyperclip
import json
from geopy.geocoders import Nominatim
from getKeys import keys

API_KEY = keys['amadeus']['private']

def getCheapestCarRentals(locationText, radius, pickUp, dropOff, returns=None):

    # Turn location string into lat, lon
    geolocator = Nominatim()
    location = geolocator.geocode(locationText)
    latitude = location.latitude
    longitude = location.longitude

    BASE_URL = "https://api.sandbox.amadeus.com/v1.2/cars/search-circle"

    res = requests.get(BASE_URL + '?apikey=' + API_KEY + '&latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&radius=' + str(radius) + '&pick_up=' + str(pickUp) + '&drop_off=' + str(dropOff))
    return_dict = json.loads(res.text)
    return(return_dict)
