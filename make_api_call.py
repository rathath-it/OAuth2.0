# How to use
# KEY=AIzaSyBrg_j1-SDkaDfO_ python
# >> from make_api_call import get_geocode_location
# >> get_geocode_location('Tunisia')
import os
import httplib2
import json


def get_geocode_location(input_string):
    google_api_key = os.environ.get('KEY')
    # replace space by +
    location_string = input_string.replace(' ' , '+')
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location_string, google_api_key))
    response, content = httplib2.Http().request(url, 'GET')
    result = json.loads(content)
    print 'response header %s \n \n' % response
    return result
