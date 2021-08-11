
from django.shortcuts import render, redirect, reverse, HttpResponse
# from Project.models import shejirenwu

# 商机附件


from django.views import View #CBV设计模式



import json
import os


class logoin_view(View):
    def __init__(self):
        super().__init__()
        self.ret = {'state': True, 'message': None}

    def get(self,request):
        try:

            title ='登录'
            return render(request, 'logoin/login.html', locals())
        except Exception as e:
            self.ret['message'] = '%s'%e
            self.ret['state'] = False
            print(e)
            return HttpResponse(json.dumps(self.ret))
    def post(self,request):
        print('Project_business add post')
        try:
            print(request.POST)
            # if Project.objects.filter(title=request.POST.get('title')).count() > 0: raise ValueError('已经存在')
            modesFrom = modefrom(request,request.POST)

            if modesFrom.is_valid():
                print('验证成功')
                obj = modesFrom.save()
                print('验证成功',obj)
                for file in request.FILES.getlist('file'):
                    filepath=os.path.join(settings.MEDIA_ROOT,Project_filepath%(obj.id,obj.id),file.name)
                    res = fileSave(file=file, filepath=filepath)

                    if res.get('err') == None:
                        Project_file.objects.create(
                            Project=obj,
                            title=file.name,
                            fileName=file.name,
                            fileSize=file.size,
                            url=res.get('filename').split(settings.BASE_DIR)[1],
                            )

                oa = create_Oa()
                rets = oa.business(obj)

                if rets.get('errcode') == 0:

                    obj.processinstanceID = rets.get('process_instance_id')
                    obj.audit_state = '1'
                    obj.save()

                    # print("reverse('sale_task')",reverse('sale_task'))
                    self.ret['url']=reverse('sale_task')
                else:
                    obj.audit_state = '0'
                    obj.save()
                    raise ValueError('%s' % rets.get('message'))
                self.ret['url']=reverse('business')

            else:
                self.ret['state'] = False
                self.ret['message'] = modesFrom.errors.get_json_data()

                

        except Exception as e:
            print('Exception', e)

            self.ret['state'] = False
            self.ret['message'] = '%s' % e


        finally:
            print('finally', self.ret)
            return HttpResponse(json.dumps(self.ret))

    def put(self, request):
        try:
            print('put')
            data = json.loads(request.body)
            print(data)
        except Exception as e:
            self.ret['state'] = False
            self.ret['message'] = e
        finally:
            return HttpResponse(json.dumps(self.ret))




    def delete(self, request):
        try:

            obj = shejirenwu.objects.get(id=request.GET.get('id'))
            data = json.loads(request.body)
            if obj.she_ji_zi_liao_set.filter(fileId=data.get('id')):
                obj.she_ji_zi_liao_set.filter(fileId=data.get('id')).delete()

        

        except Exception as e:
            self.ret['state'] = False
            self.ret['message'] = '%s' % e
        finally:
            print('finally', self.ret)
            return HttpResponse(json.dumps(self.ret))
