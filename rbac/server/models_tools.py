
def get_verbose_name(appname,modelname,exclude=[]):
    '''
    :param appname: app 名称
    :param modelname: models 名称
    :param exclude: 要排除的字段
    :return:
    '''
    from django.apps import apps
    modelobj = apps.get_model(appname,modelname) #得到Models obj
    field_dic = {}
    for field in modelobj._meta.fields:
        if field.name in exclude:continue #如果在排除列表就退出本次循环
        field_dic[field.name] = field.verbose_name
        # field_dic[field.name]['help_text'] = field.help_text
    return field_dic