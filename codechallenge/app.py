from flask import Flask, render_template, request
import requests

app = Flask(__name__)

class WeatherAppBackend:
    def __init__(self, api_key, city_name):
        self.api_key = api_key
        self.city_name = city_name
        self.standard_url = 'http://api.openweathermap.org/data/2.5/weather?'

    def get_weather_data(self):
        full_url = f"{self.standard_url}q={self.city_name}&appid={self.api_key}"
        try:
            response = requests.get(full_url)
            response.raise_for_status()
            weather_data = response.json()
            print(f"Weather Data for {self.city_name}:")
            print(f"Temperature: {weather_data['main']['temp']} K")  # Temperature in Kelvin
            print(f"Description: {weather_data['weather'][0]['description']}")
            return weather_data
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
            return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        backend = WeatherAppBackend('5dd09ae78dfe16cade77b62b87b1b292', city)  # API key here
        weather_data = backend.get_weather_data()
        if weather_data:
            return render_template('index.html', weather_data=weather_data)
        else:
            return render_template('index.html', error="Unable to fetch weather data")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
