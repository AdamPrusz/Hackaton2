from geopy.geocoders import Nominatim

def geo_lat(city):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(city)
    return location.latitude

def geo_lon(town):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(town)
    return location.longitude








