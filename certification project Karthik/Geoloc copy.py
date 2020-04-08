import geocoder  #to get the lattitude and longitude of my current location
import location
g = geocoder.ip('me')
#print(g.latlng)
city_name = input("Enter city name: ")
geoloc_city = geocoder.location(city_name)
print geoloc_city

