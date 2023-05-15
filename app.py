import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    country = request.form['country']
    url = f'http://api.weatherstack.com/current?access_key=0ddb89920d3c483dc692bf89f228f398&query={city},{country}'

    response = requests.get(url)
    data = response.json()

    if 'success' in data and not data['success']:
        error_message = data['error']['info']
        return render_template('error.html', error_message=error_message)

    temperature = data['current']['temperature']
    weather_icons = data['current']['weather_icons']
    weather_description = data['current']['weather_descriptions']

    return render_template('weather.html', city=city, country=country, temperature=temperature, weather_icons=weather_icons, weather_description=weather_description)

if __name__ == '__main__':
    app.run(debug=True)
