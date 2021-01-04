from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c3a57a5f5bff4059bbdbaeb55179b910")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})
