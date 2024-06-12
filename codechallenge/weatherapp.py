import requests

class WeatherAppBackend:
    def __init__(self, api_key):
        self.api_key = api_key
        self.city_name = "Cape Town"
        self.standard_url = 'http://api.openweathermap.org/data/2.5/weather?'

    def get_weather_data(self):
        # Constructing the full URL
        full_url = f"{self.standard_url}q={self.city_name}&appid={self.api_key}"
        
        try:
            response = requests.get(full_url)
            response.raise_for_status()  # Raises an exception if the response was not successful
            
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")

    def print_weather_details(self):
        weather_data = self.get_weather_data()
        
        if weather_data:
            main_weather_info = weather_data['main']
            min_temp = main_weather_info['temp_min'] - 273.15  # Convert Kelvin to Celsius
            max_temp = main_weather_info['temp_max'] - 273.15  # Convert Kelvin to Celsius
            humidity = main_weather_info['humidity']
            
            weather_conditions = weather_data['weather'][0]['description']
            
            print("In Cape Town it is")
            print(f"Humidity: {humidity}%")
            print(f"How Cold: {min_temp:.2f}°C")
            print(f"How Warm: {max_temp:.2f}°C")
            print(f"Weather: {weather_conditions}")

if __name__ == "__main__":
    API_key = '5dd09ae78dfe16cade77b62b87b1b292'
    weather_app = WeatherAppBackend(API_key)
    weather_app.print_weather_details()
