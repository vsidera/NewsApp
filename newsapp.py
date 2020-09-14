from flask import Flask ,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="6466c55e78594af19e719ad4539357ed")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)