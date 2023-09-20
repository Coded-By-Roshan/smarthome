from django.contrib import admin
from django.urls import path,include
from .views import home,record_audio,AudioDataView, login_page
from seller import views
urlpatterns = [
    path('', login_page, name="login_page"),
    path('home', home, name="home"),
     path('record', record_audio, name='record_audio'),
     path('audio_list', views.audio_list, name='audio_list'),
     path('audioview',AudioDataView.as_view(), name="audioview")
]