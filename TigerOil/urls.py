from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'card_list', views.card_list, name='card_list'),
    url(r'game', views.game, name='game'),
    url(r'lobby', views.lobby, name='lobby'),
]
