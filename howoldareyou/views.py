from django.http import HttpResponse
from django.shortcuts import render,redirect
from instagram.client import InstagramAPI

CLIENT_ID = "c72d5ca3e97b4e228bfe550d0ff2561b"
CLIENT_SECRET = "a23c3bb0704b4e9cbb151342e62a72ff"

def index(request):
    print dir(request)
    print request.get_raw_uri()
    result = str(request.get_raw_uri()).split('code=')[1]
    print result

    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8000")
    access_token = api.exchange_code_for_access_token(str(result))
    print access_token
    # return HttpResponse("GET ACCESSTOKEN")
    request.session['accesstoken'] = access_token
    context = {'accesstoken' : access_token}
    return render(request, 'analytics.html', context)