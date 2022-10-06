from django.shortcuts import render
from news.models import News

def testapp3_func(request, *arg, **kwarg):
    first_news=News.objects.get(id=1)
    return render(request,'testapp3/testapp3.html', {"key" : first_news})
