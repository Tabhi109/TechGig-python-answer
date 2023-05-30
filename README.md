# Weather Forecasting Tool

This command-line tool provides current weather forecasts for specified cities. It leverages the OpenWeatherMap API to fetch weather data and parses it using Python. The tool incorporates the power of GitHub Copilot to assist with API usage, data parsing, and error handling.

## Features

- **Weather Forecast**: Enter a city name to retrieve the current weather forecast.
- **Command-Line Interface**: Interact with the tool through a user-friendly command-line interface.
- **OpenWeatherMap API Integration**: Fetch real-time weather data from the OpenWeatherMap API.
- **GitHub Copilot Assistance**: Utilize AI-powered code suggestions and completion from GitHub Copilot.
- **Error Handling**: Implement robust error handling mechanisms for a reliable user experience.

## Requirements

- Python 3.x
- `requests` library (Install with `pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-forecasting-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-forecasting-tool
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the tool:

   ```bash
   python weather_tool.py
   ```

5. Follow the on-screen prompts to enter the city name and retrieve the weather forecast.

## Examples

Here are a few examples demonstrating the usage of the Weather Forecasting Tool:

```bash
$ python weather_tool.py
Enter a city name: London
Weather forecast for London:
Temperature: 15°C
Description: Partly cloudy
Humidity: 65%
Wind Speed: 10 km/h
```

```bash
$ python weather_tool.py
Enter a city name: New York
Weather forecast for New York:
Temperature: 20°C
Description: Sunny
Humidity: 55%
Wind Speed: 8 km/h
```

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## References

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Python `requests` Library Documentation](https://docs.python-requests.org/en/latest/)

## License

This project is licensed under the [MIT License](LICENSE).
