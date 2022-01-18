import requests
import json
from datetime import date

def Date():
    today = date.today()
    return today

if __name__ == '__main__':
    print(f"\nTop News of {Date()} for India : \n")
    url = f"https://newsapi.org/v2/everything?q=India&from={Date()}&sortBy=popularity&apiKey=121240d0888f4970b184de2ca684a230"
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict["articles"]
    i = 1
    for article in articles:
        print(i,"-- " + article["title"]+"\n")
        i += 1
    print("That's all for today -- ThankYou for reading :)")