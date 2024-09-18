from sys import meta_path

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',ProductViewSet.as_view({'get':'list','post':'create'}),name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete':'destroy'}), name='product_detail'),

    path('category', CategoryViewSet.as_view({'get': 'list', 'post': 'crate'}), name='category_list'),
    path('category/<int:pk>/',CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='category_detail'),

    path('comment', ProductViewSet.as_view({'get': 'list', 'post': 'crate'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='comment_detail'),


]