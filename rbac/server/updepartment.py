'''
把钉钉部门信息更新同步到本地
mail:50510661@qq.com
'''
from rbac.models import Organizational


def department(department_list):
    '''
     [{'createDeptGroup': True, 'name': '广东华晨影视舞台专业工程有限公司', 'id': 1,
      'autoAddUser': True}, {'createDeptGroup': True, 'name': '经营部', 'id': 155006637,
      'autoAddUser': True, 'parentid': 155285339}]
    :param department_list: 钉钉返回的部门List列表
    :return:
    '''


    msg = {'errcode': 0, 'info': 'OK'}
    try:
        for item in department_list:
            name=item.get('name') #部门名称
            parentid=item.get('parentid') #父部门,如果为1
            id=item.get('id') #父部门,如果为1
            if Organizational.objects.filter(dingID=id).first() == None: #如果不存在就创建
                Organizational.objects.create(
                    dingID=id,
                    title=name,
                    parentid=parentid
                )
    except Exception as e:
        msg['errcode'] = 1
        msg['info'] = '钉钉部门信息更新同步到本地 department %s'%e

    return msg
