import requests
import json

def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception if request is not successful
        data = response.json()

        # Extract relevant weather information
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", str(e))
    except (KeyError, IndexError):
        print("Failed to parse weather data. Please try again.")

API_KEY = "206d565864c5ebdb263c445f3ca630f1"
city_name = input("Enter a city name: ")
get_weather_forecast(API_KEY, city_name)
