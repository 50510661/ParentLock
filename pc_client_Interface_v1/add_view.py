from rbac.server.fenye import fenye  # 分页
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View #CBV设计模式
from django.conf import settings
import json
from conf.my_conf import token_Signature  #所有的配置文件 import
import jwt
class add_view(View):
    def __init__(self):
        super().__init__()
        self.ret = {'state': True, 'message': None}
    def get(self,request):
        print(request.GET)
        import jwt
        self.ret['message']='ads'
        print('GET')
        return HttpResponse(json.dumps(self.ret))
    def post(self,request):
        print('post',request.POST)

        return HttpResponse(json.dumps(self.ret))