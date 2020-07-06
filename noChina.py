import urllib.request
import json

class Location:
    def __init__(self, country, latitude, longitude):
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

#Extracts the IP address location 
def extractLocation(ipAddr: str):

    with urllib.request.urlopen(f"https://geolocation-db.com/json/{ipAddr}") as url:
        data = json.loads(url.read().decode())
        country = data.get('country_name')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

    countryData = (country, latitude, longitude)
    return countryData

# The "*" unpacks the tuple into a set of arguments to be passed into the function
object1 = Location(* extractLocation("1.1.1.1"))



