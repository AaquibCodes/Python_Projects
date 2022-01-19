from win32com.client import Dispatch
import requests
import json
from datetime import date

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def Date():
    today = date.today()
    return today

if __name__ == '__main__':

    speak(f"News for {Date()}")
    url = f"https://newsapi.org/v2/everything?q=India&from={Date()}&sortBy=popularity&apiKey=121240d0888f4970b184de2ca684a230"
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict["articles"]
    for article in articles:
        speak(article["title"])
        speak("next news ....")
    speak("thats all for today Thankyou ")
    print(Date())