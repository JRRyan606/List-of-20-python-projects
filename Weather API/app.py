from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Fake historical weather data (replace with your actual data source)
weather_data = {
    "new-york": [
        {"date": "2023-09-01", "temperature": 78, "humidity": 60},
        {"date": "2023-09-02", "temperature": 82, "humidity": 55},
        # Add more historical data as needed
    ],
    "los-angeles": [
        {"date": "2023-09-01", "temperature": 88, "humidity": 40},
        {"date": "2023-09-02", "temperature": 90, "humidity": 45},
        # Add more historical data as needed
    ],
}

# List of available cities
available_cities = ["New York", "Los Angeles"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_city = request.form.get('city')
        if selected_city:
            city_key = selected_city.lower().replace(' ', '-')
            if city_key in weather_data:
                weather_info = weather_data[city_key]
                return render_template('index.html', cities=available_cities, selected_city=selected_city,
                                       weather_info=weather_info)

    return render_template('index.html', cities=available_cities)


if __name__ == '__main__':
    app.run(debug=True)
