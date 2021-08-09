# coding=utf-8
#__author__=50510661@qq.com
from django.conf import settings
def init_permission(request,user):
    '''
    初始化用户权限
    :param request:
    :param user:
    :return:
    '''

    permission_queryset = user.userinfo.role.filter(permission__isnull=False).values(
        'permission__url',
        'permission__title',
        'permission__icon',
        'permission__pid',
        'permission__pid__title',
        'permission__pid__url',
        'permission__id',
        'permission__memu',
        'permission__memu__title',
        'permission__memu__icon',

    ).distinct()  # 用户所有url,去重

    # print(permission_queryset)
    MEMU_SEEION_dict={}#用户菜单
    permission_list=[]#用户权限列表
    for item in permission_queryset:
        # print('item',item)
        permission_list.append(
            {'id':item['permission__id'],
             'title':item['permission__title'],
             'url': item['permission__url'],
             'pid':item['permission__pid'],
             'ptitle':item['permission__pid__title'],
             'purl':item['permission__pid__url'],
             'picon':item['permission__icon'],



             },
                               )#将用户权限URL写入列表
        menu_id=item['permission__memu']
        if not menu_id:continue#如果ID为空就退出
        node={'id':item['permission__id'],'title':item['permission__title'],'url':item['permission__url']}
        if menu_id in MEMU_SEEION_dict:
            MEMU_SEEION_dict[menu_id]['chidren'].append(node)
        else:

            # print(item)
            MEMU_SEEION_dict[menu_id]={
                'id':item['permission__memu'],
                'title':item['permission__memu__title'],
                'chidren' : [node,],
                'icon':item['permission__memu__icon'],

            }
            # MEMU_SEEION_dict[menu_id].'chidren'=[item[node]]
    # print("*" * 100)
    # print(MEMU_SEEION_dict)



    # permission_list = [item['permission__url'] for item in permission_queryset]  # 列表生成式
    # print(permission_queryset, permission_list)
    request.session[settings.PERMISSION_SEEION_KEY] = permission_list  # 写入权限session
    request.session[settings.MEMU_SEEION_KEY]=MEMU_SEEION_dict#写入菜单权限
    return True