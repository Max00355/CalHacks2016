import amadeus
from geopy.geocoders import Nominatim
from getKeys import keys

API_KEY = keys['amadeus']['private']

def getCheapestHotels(locationText, radius, checkIn, checkOut, returns=None):

    # Set up hotels
    hotels = amadeus.Hotels(API_KEY)

    # Turn location string into lat, lon
    geolocator = Nominatim()
    location = geolocator.geocode(locationText)
    latitude = location.latitude
    longitude = location.longitude

    # Return
    return hotels.search_circle(
        latitude=latitude,
        longitude=longitude,
        radius=radius,
        check_in=checkIn,
        check_out=checkOut
    )
