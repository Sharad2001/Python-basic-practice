import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Today's News are:")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=80601be6143442da8a21e8ccb0eb0d00"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on the next news..")
    speak("Thank You!!!!")