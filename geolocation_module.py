from geopy.geocoders import Nominatim

def latitude(city):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(city)
    return location.latitude

def longtitude(town):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(town)
    return location.longitude








