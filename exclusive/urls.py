from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('login', views.login, name='login'),
    path('Main', views.Main, name='Main'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('show', views.show, name='show'),
    path('cust', views.cust, name='cust'),
    path('logout', views.logout, name='logout'),

    path('cdelete/<int:p_id>', views.cdelete, name='cdelete'),

    path('search', views.search, name="search"),
    path('searchproduct', views.searchproduct, name="searchproduct"),
]
