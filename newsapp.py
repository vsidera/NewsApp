from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="6466c55e78594af19e719ad4539357ed")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")