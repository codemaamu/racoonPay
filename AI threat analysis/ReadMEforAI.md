# News Sentiment Analysis with Python

This Python script allows you to collect and analyze news articles over the past 6-12 months based on a search query. It performs sentiment analysis on the articles and provides an organized output, highlighting the words "Positive," "Negative," or "Neutral."

## Prerequisites

Before using the script, make sure you have the following:

- A News API key: You need to sign up for a News API key from [newsapi.org](https://newsapi.org/) and replace `'YOUR_API_KEY'` in the code with your actual key.

## How to Use

1. Run the script by executing it in your terminal or code editor.
2. You will be prompted to enter a search query for news articles.
3. The script will fetch articles from the News API, perform sentiment analysis, and provide an organized output.

## Output

The output includes the following:

- Sentiment Analysis: An overall sentiment, which can be "Positive," "Negative," or "Neutral."
- Recommended Articles: A table containing the titles and URLs of articles, categorized as "Positive" or "Negative," depending on the sentiment analysis.

## Highlighted Sentiments

- The words "Positive" are highlighted in green.
- The words "Negative" are highlighted in red.

## Article Formatting

- A newline character is added between each article to leave a line space, making the output more readable.

## Note

- This script uses ANSI escape codes for text color formatting, which may not work in all terminal environments.

Enjoy analyzing news articles and discovering their sentiments!
