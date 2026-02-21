from django.urls import path

from players.models import Player
from players.views import PlayerListView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView

app_name = 'players'

urlpatterns = [
    path('', PlayerListView.as_view(), name='list'),
    path('create/',PlayerCreateView.as_view(),name='create'),
    path('edit/<int:pk>/', PlayerUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/',PlayerDeleteView.as_view(),name='delete'),

]
