from django.conf.urls import url
from appTwo import views

urlpattern = [
    url(r'^$',views.help,name='help')
]