from django.conf.urls import  url, include
from talks.views import (CreateTalk)

urlpatterns = [
    url(r'^submit_talk', CreateTalk.as_view(), name='create_talks'),
    ]
        
