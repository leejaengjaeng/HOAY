# encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

import json
from instagram.client import InstagramAPI

CLIENT_ID = "c72d5ca3e97b4e228bfe550d0ff2561b"
CLIENT_SECRET = "a23c3bb0704b4e9cbb151342e62a72ff"

def index(request):
    context = {}
    return render(request, 'home.html', context)

def getAnalytics(request):
    access_token = request.session['accesstoken'][0]
    api = InstagramAPI(access_token=access_token, client_secret=CLIENT_SECRET)

    medialists = api.user_recent_media()[0]
    print medialists

    mediacaptions = []
    for media in medialists :
        tags = media.caption.text.split("#")
        mediacaptions.append(tags[1:])

    point = 0
    db = Gwanjong.objects.all()

    frequency = {}

    for caption in mediacaptions :
        for word in caption:
            word = unicode(word).strip()
            if frequency.has_key(word) is True :
                print frequency
                print frequency.get(word)
                frequency[word] += 1
            else :
                frequency.setdefault(word, 0)
            for datum in db:
                if word.find(datum.word) is 1 :
                    point += datum.value
    import operator

    sort = sorted(frequency.items(), key=operator.itemgetter(1))

    result = {'best1' : sort[len(sort) - 1][0], 'best2' : sort[len(sort) - 2][0], 'best3' : sort[len(sort) - 3][0],
              'best1_count' : sort[len(sort) - 1][1], 'best2_count' : sort[len(sort) - 2][1], 'best3_count' : sort[len(sort) - 3][1],
              'interesting' : point}

    request.session['gwanjong'] = result

    return render(request, 'result.html')

def getToken(request):
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://bestjae.com/api/getToken")
    # api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8000/api/getToken")
    result = str(request.get_raw_uri()).split('code=')[1]
    print result

    access_token = api.exchange_code_for_access_token(str(result))

    request.session['accesstoken'] = access_token
    context = {'accesstoken': access_token}

    return render(request, 'analytics.html', context)


