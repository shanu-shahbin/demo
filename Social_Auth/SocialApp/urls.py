from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('custom-login/', views.custom_login, name='custom_login'),
    path('custom-signup/', views.custom_signup, name='custom_signup'),
]
