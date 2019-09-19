from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('signin/', views.signin, name='signin'),
]