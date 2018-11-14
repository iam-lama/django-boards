from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from boards import views
from accounts import views as accounts_views 

app_name = 'accounts'

urlpatterns = [
    url('', accounts_views.signup, name='signup'),
    ]
