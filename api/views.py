# encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect

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
        # print dir(media)
        # print media.caption
        # print dir(media.caption)
        # result = p.parse(unicode(media.caption))
        # result = p.parse(media.caption.text)
        tags = media.caption.text.split("#")
        mediacaptions.append(tags[1:])

    result = {'best1' : u'관종', 'best2' : u'관종', 'best3' : u'관종',
              'best1_count' : 3, 'best2_count' : 2, 'best3_count' : 1,
              'interesting' : 100}
    request.session['gwanjong'] = result
    print mediacaptions
    # # api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    # username = request.POST.get('username', 'None')

    # users = api.user_search(q=username)
    # recent_media, next_ = api.user_recent_media()
    # photos = []
    # for media in recent_media:
    #     print dir(media)
    #     # photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
    # print users
    # print dir(users[0])

    # recent_media, next_ = api.user_recent_media(user_id=users[0].id)
    # url = "https://api.instagram.com/v1/users/self/follows?access_token=" + access_token

    # import requests

    # result = requests.get(url)
    # print url
    # print result
    # print recent_media
    # user_id = str(access_token).split('.')[0]

    # followings = api.user_followed_by(user_id)

    # print followings
    return HttpResponse(mediacaptions)

def getToken(request):
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://bestjae.com/api/getToken")
    # api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8000/api/getToken")
    result = str(request.get_raw_uri()).split('code=')[1]
    print result

    access_token = api.exchange_code_for_access_token(str(result))

    request.session['accesstoken'] = access_token
    context = {'accesstoken': access_token}

    return render(request, 'analytics.html', context)


