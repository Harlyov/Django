from django.urls import path
from fans.views import FanCreateView, FanUpdateView, FanListView, FanDeleteView

app_name = 'fans'

urlpatterns = [
    path('', FanListView.as_view(), name='list'),
    path('create/', FanCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', FanUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', FanDeleteView.as_view(), name='delete'),

]
