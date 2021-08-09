import re
from django.conf import settings
def user_permission(request):
    '''
    处理用户权限
    :param request:
    :param user:
    :return:
    '''
    tags=False
    for url in request.session.get(settings.PERMISSION_SEEION_KEY):
        if re.match(url.get('url'),request.path_info):
            tags =True
    return tags
