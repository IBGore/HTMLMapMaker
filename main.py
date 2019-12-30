import sys
import geopy.geocoders
from geopy.geocoders import Nominatim

import folium as fol

if len(sys.argv) < 3:
    sys.exit("Too few arguements!")

geolocator = Nominatim(user_agent="HTML_Map_Maker")

try:
    start = geolocator.geocode(sys.argv[1], exactly_one=True, timeout=60)
    start.longitude

    end = geolocator.geocode(sys.argv[2], exactly_one=True, timeout=60)
    end.longitude
except AttributeError:
    sys.exit("Problem with data or cannot Geocode.")

print(start.latitude, start.longitude)
print(end.latitude, end.longitude)
