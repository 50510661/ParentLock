from rest_framework.views import APIView
from rest_framework.response import Response
# from Jwt.extensions.auth import JwtQueryParamAuthentication, JwtAuthorizationAuthentication
from conf.my_conf import token_Signature  #所有的配置文件 import
import jwt
# 获取token
from rbac.server.jwt_tools import get_token
# 验证token

class get_token_views(APIView):
    authentication_classes=[] #取消验证
    def get(self,request,*args,**kwargs):
        payload={'id':'','type':''}
        token=get_token(payload)
        ret = {'token':'jwt %s'%token.decode('utf-8')}

        return Response(ret)
    #
    # def post(self, request, *args, **kwargs):
    #     ret = {'state': True, 'message': 'login post'}
    #     print('login post')
    #     print(dir(request))
    #     token=request.data.get('token')
    #     print(token)
    #     ret['message'] = parse_payload(token)
    #     return Response(ret)
