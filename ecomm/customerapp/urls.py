from django.urls import path
from . import views


urlpatterns = [
    path('sinup/', views.sinup, name='sinup'),
    path('loggg/', views.loggg, name='loggg'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]
