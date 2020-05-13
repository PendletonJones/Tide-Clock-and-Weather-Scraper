#This URL is the page you actually want to pull down with requests
#My API Key must be used at the end of the requested URL with '&APPID=02ef7d3c631464e3f8249a426469f7dc'
#request_url ='https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02'

import requests

def poq_weath():
    #This is the URL that your login form poits to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat=37.1&lon=-76.3&appid=02ef7d3c631464e3f8249a426469f7dc'

    #Dictionary to create login payload
    #OpenWeatherMap API Key  '02ef7d3c631464e3f8249a426469f7dc'

    payload = {
        'username': '***********',
        'pass': '*************'
        }



    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        precip = r.json()["weather"]


        for item in precip:
            return item["description"]
            # print(item["description"])

def poq_wind():
    #This is the URL that your login form poits to with the "action" tag
    post_login_url = 'https://home.openweathermap.org/users/sign_in'

    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat=37.1&lon=-76.3&appid=02ef7d3c631464e3f8249a426469f7dc'

    #Dictionary to create login payload
    #OpenWeatherMap API Key  '02ef7d3c631464e3f8249a426469f7dc'

    payload = {
        'username': '*********',
        'pass': '*************'
        }


    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        wind = r.json()["wind"]
        wind_current = wind["speed"]
        return wind_current
