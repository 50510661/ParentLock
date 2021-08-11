# coding=utf-8
#__author__=50510661@qq.com
from django.urls import path,include,re_path
from .push_pc_base_info import push_pc_base_info_view
from .push_imgs_view import push_imgs_view
from .get_token_views import get_token_views
urlpatterns = [
    re_path('get_token/$',get_token_views.as_view(),name='get_token'),
    re_path('push_pc_base_info/$',push_pc_base_info_view.as_view(),name='push_pc_base_info'),
    re_path('push_imgs$',push_imgs_view.as_view(),name='pc_push_imgs'),


]