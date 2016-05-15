from django.http import HttpResponse
from django.shortcuts import render,redirect
from instagram.client import InstagramAPI
from django.template.response import TemplateResponse

CLIENT_ID = "c72d5ca3e97b4e228bfe550d0ff2561b"
CLIENT_SECRET = "a23c3bb0704b4e9cbb151342e62a72ff"

def index(request):
    api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://bestjae.com/api/getToken")
    # api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8000/api/getToken")
    redirect_uri = api.get_authorize_login_url(scope=["basic", "public_content", "follower_list"])
    #return HttpResponse("<a href=" + redirect_uri + ">Instagram</a>")
    #request.session['redirect'] = redirect_uri
    context = {'re' : redirect_uri}
    #return render(request, "index.html", context)
    return TemplateResponse(request, "index.html", context)
