from django.urls import path
from .views import CommentCreateView

app_name = 'comments'

urlpatterns = [
    path('add/', CommentCreateView.as_view(), name='add'),
]