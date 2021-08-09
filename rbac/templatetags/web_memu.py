# coding=utf-8
# __author__=50510661@qq.com
from django.template import Library
from django.conf import settings
from collections import OrderedDict
import re
from rbac.models import Permission #二级菜单

register = Library()  # 固定写法不能改变


@register.inclusion_tag('rbac/static_memu.html')
def static_memu(request):
    '''
    创建一级菜单
    :return:
    '''
    memu_list = request.session.get(settings.MEMU_SEEION_KEY)
    # print(memu_list)
    # print('*'*100)
    return {'memu_list': memu_list,'request':request}
@register.inclusion_tag('rbac/breadcrub.html')
def breadcrub(request):
    '''用户访问记录'''
    return {'breadcrumb_list': request.breadcrumb}

@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    '''
    二级菜单生成
    :param request:
    :return:
    '''
    menu_dict=request.session.get(settings.MEMU_SEEION_KEY)
    # 对字典的key进行排序
    # print('menu_dict',menu_dict)
    key_list = sorted(menu_dict)
    # print('key_list',key_list)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        # print('request.session[settings.PERMISSION_SEEION_KEY]',request.session[settings.PERMISSION_SEEION_KEY])
        # print('-'*100)
        val = menu_dict[key]
        # print('val',val)
        val['class'] = 'hide'

        for per in val['chidren']:
            regex = "^%s$" % (per['url'],)
            # print('request.session[settings.PERMISSION_SEEION_KEY]', request.session[settings.PERMISSION_SEEION_KEY])
            # print('request.session[PERMISSION_SEEION_KEY]',request.session[settings.PERMISSION_SEEION_KEY])
            if request.current_selected_permission == per['id']:
                # print('per', per)

                per['class'] = 'active'
                val['class'] = ''

        ordered_dict[key] = val


    return {'menu_dict':ordered_dict,'request':request}
