# coding=utf-8
#__author__=50510661@qq.com
from django.urls import path,include,re_path
from .logoin_view import logoin_view

urlpatterns = [
    re_path('',logoin_view.as_view(),name='login'),
]