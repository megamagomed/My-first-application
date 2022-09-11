from django.shortcuts import render

def testapp2_func(request, *arg, **kwarg):
    return render(request, 'testapp2/testapp2.html', {'context2': 34567})
