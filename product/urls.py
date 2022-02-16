from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('product_create', views.product_create, name='product_create'),
    path('create', views.create, name='create'),
    path('Sale/', views.Sale, name='Sale'),
    path('pupdate/<str:p_id>', views.pupdate, name='pupdate'),
    path('pdelete/<int:p_id>', views.pdelete, name='pdelete')


]
