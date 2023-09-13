## Positive News Site
A web application that retrieves news articles from a news API and publishes only positive news based on sentiment analysis.

## Features
Fetches news articles from a News API (you need to provide your API key).
Performs sentiment analysis on news article titles.
Displays only positive news articles on the web page.

## Getting Started
Replace 'your_news_api_key' in app.py with your News API key.

Install the required libraries:

`pip install requests flask vaderSentiment`

## Run the application:

`python app.py`

Open your web browser and navigate to http://localhost:5000 to see positive news articles.