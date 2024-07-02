
# A very simple Flask Hello World app for you to get started with...



from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'


import requests

app = Flask(__name__)

@app.route('/api/hello/', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr

    # Get location data
    # location_response = requests.get(f'https://ipihttpsnfo.io/{client_ip}/json')
    # location_data = location_response.json()
    location_data = {

        "city": "New York"

        }

    city = location_data.get('city')
    # region = location_data.get('region')
    # country = location_data.get('country')

    # Get temperature data (using OpenWeatherMap API)
    api_key = '120f62a89e99bf1e4d8834934e145539'
    weather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    response = {
        'message': f'Hello, {visitor_name}, the temperature is {temperature} degree celcius in {city}!',
        'ip': client_ip,

    }

    return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)
