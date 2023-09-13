from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = '829b55d9eecaf06acfb172f5fe4f2c32'
OPENWEATHERMAP_BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

@app.route('/', methods=['GET', 'POST'])
def index():
    city = None
    forecast_data = []
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            forecast_data, error_message = get_weather_forecast(city)

    return render_template('index.html', city=city, forecast_data=forecast_data, error_message=error_message)

def get_weather_forecast(city):
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(OPENWEATHERMAP_BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        forecast = data.get('list', [])
        return process_forecast_data(forecast), None
    else:
        return [], 'City not found or API error'

def process_forecast_data(forecast):
    forecast_data = []

    for entry in forecast:
        timestamp = entry.get('dt', 0)
        temperature = entry.get('main', {}).get('temp', 0)
        date = entry.get('dt_txt', '')
        forecast_data.append({'date': date, 'temperature': temperature})

    return forecast_data[:5]  # Get the next 5 days' data

if __name__ == '__main__':
    app.run(debug=True)
