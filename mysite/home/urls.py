from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
   path('play-game/', views.play_game, name='play_game' ),
]
