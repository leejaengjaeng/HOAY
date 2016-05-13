from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'getAnalytics$', views.getAnalytics, name='getAnalytics'),
    url(r'getToken$', views.getToken, name='getToken'),
]