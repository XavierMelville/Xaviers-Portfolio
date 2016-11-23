from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.card_list, name='card_list'),
]
