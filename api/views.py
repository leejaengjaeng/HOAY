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

    from itp import itp
    p = itp.Parser()

    mediacaptions = []
    for media in medialists :
        # print dir(media)
        # print media.caption
        # print dir(media.caption)
        # result = p.parse(unicode(media.caption))
        # result = p.parse(media.caption.text)
        tags = media.caption.text.split("#")
        mediacaptions.append(tags[1,])

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
    return HttpResponse("AA")

def getToken(request):
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8000")
    redirect_uri = api.get_authorize_login_url(scope=["basic", "public_content", "follower_list"])

    print redirect_uri

    # import requests
    # from bs4 import BeautifulSoup
    # result = requests.get(redirect_uri)
    # bs = BeautifulSoup(result.text)
    #
    # table = bs.find('table', 'meta')
    # print table
    # accesstoken = api.exchange_code_for_access_token("fbc4f97f0c0346628982cc2e8ea3e675")
    # accesstoken = api.exchange_code_for_access_token()
    # print accesstoken

    return HttpResponse("<a href=" + redirect_uri + ">GOGO</a>")


