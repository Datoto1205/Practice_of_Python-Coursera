import urllib.request, urllib.parse, urllib.error
import json

serviceURL = "http://maps.googleapis.com/maps/api/geocode/json?address="

while True:
    '''Because now Google Geocoding API require a API key,
       we could not use the code below to fetch the JSON code anymore;
       Therefore, I attached the JSON code below directly.'''
    # address = input("Enter the location: ")
    # if len(address) < 1:
    #     break
    #
    # finalURL = serviceURL + urllib.parse.urlencode({'address', address})
    #     # Get the address of the location and transform it into the right form.
    # print("Retrieving", url)
    # rawData = urllib.request.urlopen(finalURL)
    # data = rawData.read().decode()
    # print("Retrieving", len(data), "characters")
    # # Fetch the data from the server.

    data = '''{
      "status": "OK",
      "result": [
        {
          "geometry": {
            "location_type": "APPROXIMATE",
            "location": {
              "lat": 25,
                "lng": 0
            }
          },
          "address_components": [
            {
              "long_name": "Columbia University",
                "types": [
                  "locality",
                    "political"
                ],
                "short_name": "Columbia University"
            }
          ],
          "formatted_address": "Columbia University, NYU, USA",
          "types": [
            "locality",
              "political"
          ]
        }
      ]
    }'''

    try:
        js = json.loads(data)
        # Identify wgether the data we get is JSON or not.
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("=====Failure to fetch the data!=====")
        print(data)
        continue

    print(json.dumps(js, indent = 4))   # Organize the JSON data.


    latitude = js['result'][0]['geometry']['location']['lat']
    longtitude = js['result'][0]['geometry']['location']['lng']
    finalAddress = js['result'][0]['formatted_address']
    print("The location of the place-" + finalAddress + "-is at (" + str(latitude) + ", " + str(longtitude) + ").")
    break
