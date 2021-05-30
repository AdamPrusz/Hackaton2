from geopy.geocoders import Nominatim



# def geo_location():
#     locator = Nominatim(user_agent='myGeocoder')
#     location = locator.geocode(input("Give me street, city or country name --> "))
#     return [location.latitude, location.longitude]

def geo_lat(city):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(city)
    return location.latitude

def geo_lon(town):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(town)
    return location.longitude








