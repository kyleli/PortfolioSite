from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter/', views.counter, name='counter'),
    path('lucy/', views.lucy, name='lucy'),
    path('statictest/', views.statictest, name='statictest'),
    path('wordcounter', views.wordcounter, name='wordcounter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]