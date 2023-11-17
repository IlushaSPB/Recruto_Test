from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth_random/', views.auth_random, name='auth_random'),
    path('', views.random_code),
    path('auth/', include('django.contrib.auth.urls')),
]
