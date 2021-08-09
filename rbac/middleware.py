# coding=utf-8
#__author__=50510661@qq.com
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect,reverse
from django.conf import settings
import re
class CheckPermission(MiddlewareMixin):
    '''检查URL中间件'''
    def process_request(self,request):
        """
        当用户请求时检查URL
        :param request:
        :return:
        """
        current_url=request.path_info#当前URL
        permission_URL_list=request.session.get(settings.PERMISSION_SEEION_KEY)#用户权限列表

        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url,current_url):#匹配成功白名称就退出
                return None
        if not permission_URL_list:#如果列表为空就说明没有登录
            print('请重新登录')
            return redirect(reverse('login'))
            # return HttpResponse('请重新登录')
        flag = False  # 匹配成功标志
        url_record=[{'title':'首页','url':'#'}]#用户访问记录
        for url in permission_URL_list:
            # print('url\n',url)
            reg=url['url']
            # print('reg\n',reg)
            if re.match(reg,current_url):
                #匹配成功就退出
                flag=True
                request.current_selected_permission=url['pid'] or url['id']
                if not url['pid']:#添加用户记录
                    url_record.extend([
                        {'title':url['title'],'url':url['url'],}
                    ])
                else:
                    url_record.extend([
                        {'title': url['title'], 'url': url['url'] },
                        {'title':url['ptitle'],'url':url['purl']}
                    ])
                request.breadcrumb=url_record
                # print('用户访问记录\n',request.breadcrumb)
                break
        if not flag:
            print('没有权限访问')
            return redirect(reverse('login'))
            # return HttpResponse('没有权限访问')

        return None













