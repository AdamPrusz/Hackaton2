from geopy.geocoders import Nominatim

def geo_location():
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(input("Give me street, city or country name -->"))
    lat = 'Latitude = {}'.format(location.latitude)
    long = 'Longitude = {}'.format(location.longitude)

    return lat, long