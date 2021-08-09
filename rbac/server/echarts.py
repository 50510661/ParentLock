'''
echarts 相关方法
'''
from django.conf import settings
from rbac.models import Organizational, UserInfo, Role  # 部门表
def zhu_zhuang_tu(state,org_list,title,models):
    '''
    柱状图

    :param state: 项目状态
    :param org_list: 部门列表
    :return:
    '''
    shejishi_list=[] #人员列表
    legend = []  # 项目状态
    series = []  ##项目状态数据
    for item in state:
        legend.append(item[1])

        series.append({
            'name': item[1],
            'type': 'bar',
            'data': []
        })

    for org in org_list:
        for item in UserInfo.objects.filter(organizational__pk=org, is_active=True, is_management=False):
            shejishi_list.append(item.name)
            for i in state:
                for s in series:
                    if s.get('name') == i[1]:
                        if models == 'project':
                            s['data'].append(item.user.project_set.filter(state=i[0]).count())
                        elif models == 'shejirenwu':
                            s['data'].append(item.shejirenwu.filter(shejijieduan=i[0]).count())
                            # print(item.shejirenwu.filter(shejijieduan=i[0]).count(),item,shejirenwu)

    data = {'title': {'text': title},
            'tooltip': {},
            'legend': {
                'data': legend
            },
            'xAxis': {
                'data': shejishi_list
            },
            'yAxis': {},
            'series': series
            }
    return data

def project_zhu_zhuang_tu(state,org_list,title,models):
    '''
    项目柱状图

    :param state: 项目状态
    :param org_list: 部门列表
    :return:
    '''
    shejishi_list=[] #人员列表
    legend = []  # 项目状态
    series = []  ##项目状态数据
    for item in state:
        legend.append(item[1])

        series.append({
            'name': item[1],
            'type': 'bar',
            'data': []
        })

    for org in org_list:
        for item in UserInfo.objects.filter(organizational__pk=org, is_active=True, is_management=False): #所有该部门下活跃用户，在职用户
            shejishi_list.append(item.name)
            for i in state:
                for s in series:
                    if s.get('name') == i[1]:
                        if models == 'project':
                            s['data'].append(item.user.project_set.filter(state=i[0]).count())
                        elif models == 'shejirenwu':
                            s['data'].append(item.shejirenwu.filter(shejijieduan=i[0]).count())
                            # print(item.shejirenwu.filter(shejijieduan=i[0]).count(),item,shejirenwu)

    data = {'title': {'text': title},
            'tooltip': {},
            'legend': {
                'data': legend
            },
            'xAxis': {
                'data': shejishi_list
            },
            'yAxis': {},
            'series': series
            }
    return data