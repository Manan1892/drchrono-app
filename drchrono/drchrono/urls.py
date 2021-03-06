"""drchrono URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^Home$', HomeView.as_view(), name='home_view'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^sendmail$', SendmailView.as_view(), name='sendmail'),
    url(r'^', include('social.apps.django_app.urls', namespace='social'))

]
