from rest_framework.views import APIView
from rest_framework.response import Response
class push_pc_base_info_view(APIView):


    def post(self,request,*args,**kwargs):
        print('add post',request.POST)


        return Response({'aaa':'aa'})