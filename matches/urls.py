from django.urls import path
from matches.views import MatchCreateView, MatchUpdateView, MatchDeleteView, MatchListView

app_name = 'matches'

urlpatterns = [
    path('create/', MatchCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MatchUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MatchDeleteView.as_view(), name='delete'),
    path('', MatchListView.as_view(), name='list'),
]
