"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import index, detail_view, test_view, create_view
from testapp.views import testapp_func
from testapp2.views import testapp2_func
from testapp3.views import testapp3_func

urlpatterns = [
    path('', index),
    path('id/<int:pk>/', detail_view),
    path('test_view', test_view),
    path('news/create/', create_view),
    path('admin/', admin.site.urls),
    path('testapp', testapp_func),
    path('testapp2', testapp2_func),
    path('testapp3', testapp3_func),
]
