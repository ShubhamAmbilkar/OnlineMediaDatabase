"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myapp.views import movie_form , abstracter , action_movies , thriller_movies , best_movies

from django.contrib import admin
from django.urls import path
from myapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index , name = 'index'),
    path('media/', movie_form , name = 'media') ,
    path('abstract/' , abstracter , name = 'abstract') ,

    path('action/' , action_movies , name = 'action') ,
    path('thriller/' , thriller_movies , name = 'thriller') ,
    path('best/' , best_movies , name = 'best') ,

    path('raid/' , v.raid , name = 'raid' )
]
