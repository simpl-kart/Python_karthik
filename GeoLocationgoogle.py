import googlemaps

gmaps = googlemaps.Client(key='********************')

# Geocoding an address
geocode_result = gmaps.geocode('Thuckalay')
print geocode_result


# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((12.9791198, 77.5912997))
print reverse_geocode_result
