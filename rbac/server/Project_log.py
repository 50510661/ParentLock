 # 添加项目日志
 # 2020-06-05
 # 张军
 # 505010661@qq.com
from proj_log.models import proj_log #项目日志
def creat_project_log(request,projectObj,content):
    '''

    :param projectObj:  项目obj
    :param content: 要添加的内容
    :return:
    '''
    msg = {'state': 0, 'info': 'OK'}
    try:
        proj_log.objects.create(project=projectObj,
                                content='%s   %s' % (request.user.userinfo, content)
                                ).save  # 写入日志
    except Exception as e:
        msg['state'] = 1
        msg['info'] = '添加项目日志出错 %s'%e
        return msg
    return None
