# tracker1.py
# track location with the map using the phone number
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

from opencage.geocoder import OpenCageGeocode

# taking input the phonenumber along with the country code
number = input("Enter the PhoneNumber with the country code : ")
# Parsing the phonenumber string to convert it into phonenumber format
phoneNumber = phonenumbers.parse(number)

# Storing the API Key in the Key variable
Key = " Enter your Api"  # generate your api https://opencagedata.com/api

# Using the geocoder module of phonenumbers to print the Location in console
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("location : " + yourLocation)

# Using the carrier module of phonenumbers to print the service provider name in console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("service provider : " + yourServiceProvider)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")

#Now for the final step, we save the map in HTML file format that can be later viewed in
# a browser.
#The file will be created in the same file as the project with the name that we have given
# in the code(Location.html)

#save the map to an HTML file to open it and see the actual location in map format
