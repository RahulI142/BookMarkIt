from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_create'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('add/', views.add_post, name='add_post'),
]
