#!/usr/bin/env python3
import re
import math

import os
from dotenv import load_dotenv

# Load the environment variables from .env.
load_dotenv()
apiKey = os.getenv("API")


def validatePostCode(postcode):

  # UK postcodes are variable-length alphanumerics, 6-8 characters (including a space). 
  # The two parts, separated by a single space, are the outward and the inward code respectively.
  
  #The following regex pattern works for all geographic postcodes (not all special cases like BFPO's)
  pattern = '^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$'

  if re.match(pattern, postcode):
    return True
  else:
    return False

def returnCoordsFromPC(postcode):
  return True

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
  return round(R * c, 4)




if __name__ == '__main__':
  fromPostCode = "" 
  toPostCode = "" 

  print("This calculates the distance between two UK postcodes.")
  # Ask the user for two post codes and store them as two variables
  while validatePostCode(fromPostCode) is False:
    fromPostCode = input("Enter the start postcode: ").upper()

  while validatePostCode(toPostCode) is False:
    toPostCode = input("Enter the destination postcode: ").upper()

  # Get the actual coordinates of both post codes.
  startPoint = returnCoordsFromPC(fromPostCode)
  endPoint = returnCoordsFromPC(toPostCode)

  # Now we have two geographic points, we can use the Haversine formula 
  # to calculate the distance (as the crow flies) between the two points
  print(returnDistance(52.2296756,21.0122287,52.406374,16.9251681))


