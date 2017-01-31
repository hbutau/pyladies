from django.conf.urls import  include, url

from django.contrib import admin

from .views import SignUpView, LoginView

urlpatterns = [
    url(r'accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'accounts/login/$', LoginView.as_view(), name='login'),

]
