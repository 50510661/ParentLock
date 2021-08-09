from rbac.server.fenye import fenye  # 分页
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View #CBV设计模式
from django.conf import settings
import json
class push_imgs_view(View):
    def __init__(self):
        super().__init__()
        self.ret = {'state': True, 'message': None}
    def get(self,request):
        print(request.GET)
        print('GET')
        return HttpResponse()
    def post(self,request):
        print('post',request.POST)

        return HttpResponse(json.dumps(self.ret))