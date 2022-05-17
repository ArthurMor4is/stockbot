from newscatcherapi import NewsCatcherApiClient
import os

API_KEY = os.getenv('NEWS_API_KEY', None)

newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)

news_articles = newscatcherapi.get_search(q="Tesla")
