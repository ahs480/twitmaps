from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Topics

def index(request):
    all_topics = Topics.objects.all()
    context = {
        'all_topics' : all_topics,
    }
    return render(request, 'maps/index.html', context)



def details(request, topic_id):
    apnd = Topics.objects.get(pk = topic_id)
    awslink = ''
    full = awslink + apnd.topic
  
    tweet = requests.get(full)
    results = json.loads(tweet.text)
    round1 = results["hits"]["hits"]
    list1 = []
    for i in range(len(round1)):
        try:
            list1.append({'latitude': round1[i]['_source']['latitude'], 'longitude': round1[i]['_source']['longitude']})
        except KeyError:
            pass
    print (list1)
    context = {'list1': list1}
    return render(request, 'maps/details.html', context)

