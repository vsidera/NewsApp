from flask import Flask ,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="6466c55e78594af19e719ad4539357ed")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        

    mylist = zip(news,desc,link,img)

    return render_template('index.html' , context= mylist)

@app.route("/bbc")
def bbc():
    newsapi = NewsApiClient(api_key="6466c55e78594af19e719ad4539357ed")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        link.append(myarticles['url'])
        img.append(myarticles['urlToImage'])
        

    mylist = zip(news,desc,link,img)

    return render_template('bbc.html' , context= mylist)

if __name__ == '__main__':
    app.run(debug=True)