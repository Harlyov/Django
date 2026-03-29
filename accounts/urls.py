from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView
app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]