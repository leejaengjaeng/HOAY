from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def good(request):
    return HttpResponse("YO MAN")

def fail(request):
    return HttpResponse("YO MAN!!!")


