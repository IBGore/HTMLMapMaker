import sys
import geopy.geocoders
from geopy.geocoders import Nominatim

import folium

#Check if command line input is valid
if len(sys.argv) < 3:
    sys.exit("Too few arguements!")

#Start Cordinate API Agent
geolocator = Nominatim(user_agent="HTML_Map_Maker")

#Test if results returned sucessfuly
try:
    start = geolocator.geocode(sys.argv[1], exactly_one=True, timeout=60)
    start.longitude

    end = geolocator.geocode(sys.argv[2], exactly_one=True, timeout=60)
    end.longitude
except AttributeError:
    sys.exit("Problem with data or cannot Geocode.")

#Find map center
midlat = (start.latitude + end.latitude) / 2
midlon = (start.longitude + end.longitude) / 2

#create map
m = folium.Map(location=[midlat, midlon], tiles='OpenStreetMap')

#add location markers
folium.Marker([start.latitude, start.longitude], popup= str.title(sys.argv[1]), tooltip='Start Location', icon= folium.Icon(color='blue')).add_to(m)
folium.Marker([end.latitude, end.longitude], popup= str.title(sys.argv[2]), tooltip='Destination', icon= folium.Icon(color='red')).add_to(m)

#find map bounds
southwest = [0,0]
northeast = [0,0]

if start.latitude < end.latitude:
    southwest[0] = start.latitude
    northeast[0] = end.latitude
else:
    southwest[0] = end.latitude
    northeast[0] = start.latitude

if start.longitude < end.longitude:
    southwest[1] = start.longitude
    northeast[1] = end.longitude
else:
    southwest[1] = end.longitude
    northeast[1] = start.longitude



m.fit_bounds([southwest, northeast])

m.save("test.html")

