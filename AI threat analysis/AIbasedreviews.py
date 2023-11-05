import requests
from textblob import TextBlob
from prettytable import PrettyTable
#from datetime import datetime, timedelta

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'ffa75fbf0b4d466b851be719a209ba3a'

# Prompt the user for a search query
search_query = input("Enter a search query for news: ")

# # Calculate the date range (6-12 months ago)
# end_date = datetime.now()
# start_date = end_date - timedelta(days=365)

# from_date = start_date.strftime('%Y-%m-%d')
# to_date = end_date.strftime('%Y-%m-%d')

# Define parameters for the news search
params = {
    'apiKey': api_key,
    'q': search_query,
    'language': 'en',
    'pageSize': 20,
#     'from': from_date,
#     'to': to_date
 }

# Make a request to the News API
response = requests.get('https://newsapi.org/v2/everything', params=params)

if response.status_code == 200:
    news_data = response.json()
    articles = news_data.get('articles', [])

    positive_articles = PrettyTable(["Title", "URL"])
    negative_articles = PrettyTable(["Title", "URL"])

    for article in articles:
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')

        analysis = TextBlob(description)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            positive_articles.add_row([f"\033[92mPositive\033[0m\n{title}", url])
        elif polarity < 0:
            negative_articles.add_row([f"\033[91mNegative\033[0m\n{title}", url])

    positive_count = len(positive_articles.get_string().splitlines()) - 2  # Subtract 2 for header and separator lines
    negative_count = len(negative_articles.get_string().splitlines()) - 2

    if positive_count > negative_count:
        overall_sentiment = "\033[92mPositive\033[0m"
        recommended_articles = positive_articles
    elif positive_count < negative_count:
        overall_sentiment = "\033[91mNegative\033[0m"
        recommended_articles = negative_articles
    else:
        overall_sentiment = "Neutral"
        recommended_articles = None

    print(f"Sentiment Analysis for '{search_query}' over the past 6-12 months:")
    print(f"Overall Sentiment: {overall_sentiment}")

    if recommended_articles:
        print(f"Recommended {overall_sentiment} Articles:")
        print(recommended_articles)
    else:
        print("No specific recommendations.")
else:
    print("Error: Unable to fetch news data.")
