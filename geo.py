#!/usr/bin/env python3
import re
import math
import json
import requests
import logging

# Logging Setup
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', filename='geo.log', filemode='w', level=logging.INFO)

def validatePostCode(postcode):

  # UK postcodes are variable-length alphanumerics, 6-8 characters (including a space). 
  # The two parts, separated by a single space, are the outward and the inward code respectively.
  
  #The following regex pattern works for all geographic postcodes (not all special cases like BFPO's)
  pattern = '^[A-Za-z]{1,2}[0-9][a-zA-Z0-9]?\s*[0-9][a-zA-Z]{2}$'

  if re.match(pattern, postcode):
    return True
  else:
    return False

def returnCoordsFromPC(postcode):
  coordLat = ""
  coordLong = ""

  # To find out the cooridnates from the passed postcode, 
  # we will use the following endpoint from https://postcodes.io/ which is free to use.
  # GET ==>> api.postcodes.io/postcodes/BH189NX
  # It returns JSON with a "status": and "result" fields with longitude & latitude being what we are after.

  getURL = "https://api.postcodes.io/postcodes/"

  response = requests.get(getURL + postcode)

  if response.status_code == 200:
    data = json.loads(response.text)
    if int(data["status"]) == 200:
      return data["result"]["latitude"], data["result"]["longitude"]
    else:
      logging.warning(f'Status: {data["status"]}. Error: {data["error"]}.')
      return None, None
  else:
    return None, None


def returnDistance(lat1, lon1, lat2, lon2):
  #Radiuus of the Earth
  R = 6373.0

  # Coordinates must be converted to radians for the calculations to be correct
  lat1 = math.radians(lat1)
  lon1 = math.radians(lon1)
  lat2 = math.radians(lat2)
  lon2 = math.radians(lon2)

  # Calculate the change in coordinates
  dlon = lon2 - lon1
  dlat = lat2 - lat1

  # Haversine formula
  a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  # Return the distance, rounded to 4 decimal places.
  return round(R * c, 2)




if __name__ == '__main__':
  startPostCode = "" 
  endPostCode = "" 

  print("This calculates the distance between two UK postcodes.")
  # Ask the user for two post codes and store them as two variables
  while validatePostCode(startPostCode) is False:
    startPostCode = input("Enter the start postcode: ").upper()

  while validatePostCode(endPostCode) is False:
    endPostCode = input("Enter the destination postcode: ").upper()

  # Get the actual coordinates of both post codes.
  startLat,startLon = returnCoordsFromPC(startPostCode)
  endLat,endLon = returnCoordsFromPC(endPostCode)
  print("Coordinates for {}: {}, {}".format(startPostCode, startLat, startLon))
  print("Coordinates for {}: {}, {}".format(endPostCode, endLat, endLon))

  # Now we have two geographic points, we can use the Haversine formula 
  # to calculate the distance (as the crow flies) between the two points
  if None not in (startLat,startLon,endLat,endLon):
    distance = returnDistance(startLat,startLon,endLat,endLon)
    print("Distance between {} and {} is {}km.".format(startPostCode, endPostCode, distance))
  else:
    print("Sorry, we couldn't calculate the distance between {} and {}.".format(startPostCode, endPostCode))

