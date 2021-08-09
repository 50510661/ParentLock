# coding=utf-8
#__author__=50510661@qq.com
from django.urls import path,include,re_path
from .add_view import add_view
from .push_imgs_view import push_imgs_view
urlpatterns = [
    re_path('add/$',add_view.as_view(),name='pc_add'),
    re_path('push_imgs$',push_imgs_view.as_view(),name='pc_push_imgs'),


]