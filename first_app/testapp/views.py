from django.shortcuts import render
from news.models import News

def testapp_func(request, *arg, **kwarg):
    allnews = News.objects.all()
    return render(request, 'testapp/testapp.html', {'context': allnews})
