import os.path
import sys
import apiai
import json
import config
import Weather


def main(msg):
    ai = apiai.ApiAI(config.APIAI_CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.query = msg
    response = request.getresponse()
    string_data = str(response.read(), 'UTF-8')
    # print(string_data)
    json_data = json.loads(string_data)
    location = json_data['result']['parameters']['geo-city']
    return Weather.main(location)
    
