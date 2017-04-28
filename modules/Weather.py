import requests
import config

def main(location):
        URL = 'http://api.openweathermap.org/data/2.5/weather?q=' + str(location)+ '&units=metric&appid=' + config.OWM_CLIENT_ACCESS_TOKEN
        data = requests.get(URL)
        json_data = data.json()
        temp_c = json_data['main']['temp']
        condition = json_data['weather'][0]['description']
        return [temp_c, condition, location]

if __name__ == '__main__':
    main()