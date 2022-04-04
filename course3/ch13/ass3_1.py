import urllib.request, urllib.parse, urllib.error
import json

server = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter Location: ')
    if len(address) < 1 or address == 'done': break
    url = server + urllib.parse.urlencode({"address":address})
    print('Retreiving: ', url)
    file = urllib.request.urlopen(url).read()
    data = file.decode()
    try :
        js = json.loads(data)
    except :
        js = None
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('/////Failed to retrieve//////')
        print(data)
        continue
    id = js["results"][0]["place_id"]
    print("Place ID: ", id)
