import requests
from flask import Flask, render_template

# Import the SentimentIntensityAnalyzer class from vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

# Your News API key
NEWS_API_KEY = '25c154b58cfe41b48059b62faf31de9a'

# Define the endpoint for the News API
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines?'

# Define the parameters for the News API request
NEWS_API_PARAMS = {
    'country': 'us',  # Change the country as needed
    'apiKey': NEWS_API_KEY,
    'pageSize': 10,  # Number of news articles to fetch
}


# Function to fetch news data from the News API
def get_news():
    response = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
    news_data = response.json()
    return news_data['articles']


# Function to perform sentiment analysis
def analyze_sentiment(news):
    analyzer = SentimentIntensityAnalyzer()
    for article in news:
        text = article['title']
        sentiment_score = analyzer.polarity_scores(text)
        sentiment = sentiment_score['compound']
        article['sentiment'] = sentiment


# Function to filter and return positive news
def get_positive_news(news):
    positive_news = [article for article in news if article['sentiment'] > 0.2]
    return positive_news


@app.route('/')
def index():
    news = get_news()
    analyze_sentiment(news)
    positive_news = get_positive_news(news)
    return render_template('index.html', positive_news=positive_news)


if __name__ == '__main__':
    app.run(debug=True)
