from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    resp = '''Rango says hey there partner!
    <a href="/rango/about/">About</a>
    '''
    return HttpResponse(resp)


def about(request):
    resp = '''Rango says here is the about page.
    <a href="/rango/">Index</a>
    '''
    return HttpResponse(resp)
