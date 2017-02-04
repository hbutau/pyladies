"""harare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from pyladies_harare import views
from django.conf.urls import include, url
import accounts.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'about', views.AboutView.as_view(), name='about'),
    url(r'meetups', views.MeetupsView.as_view(), name='meetups'),
    url(r'upcoming', views.UpcomingView.as_view(), name='upcoming'),
    url(r'past', views.PastMeetupsView.as_view(), name='past'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'contact', views.ContactView.as_view(), name='contact'),
    url(r'^', include('talks.urls', namespace = 'talks')),
    url(r'^', include(accounts.urls, namespace='accounts')),
]
