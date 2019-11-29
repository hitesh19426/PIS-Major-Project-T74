import geocoder
from geopy.geocoders import Nominatim
 
def location():
	g = geocoder.ip('me')
	return  g.latlng

coord = location()

def address():

	geolocator = Nominatim()
	location = geolocator.reverse(coord)
	return (coord,location.address)