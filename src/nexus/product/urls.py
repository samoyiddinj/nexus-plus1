from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_product, name='create-product'),
    path('detail/', views.detail_product, name='detail-product')
]
