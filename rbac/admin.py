from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserinfoAdmin(admin.ModelAdmin):
    '''

    '''
    # 排除字段
    exclude = []
    # 显示字段
    list_display = (
        'user', 'telphome', 'name', 'userSource', 'unionid', 'openid', 'userid', 'position', 'active', 'avatar',
        'email',
    )
    #

    # 分类显示
    fieldsets = [
        ('用户基础信息', {'fields': [('user', 'telphome', 'email'), ('name')]}),
        ('钉钉信息', {'fields': [('unionid', 'openid', 'position')]}),
        ('角色信息', {'fields': [('role',)]}),
        ('开关信息', {'fields': [('is_management', 'is_active')]}),
    ]
admin.site.register(UserInfo,UserinfoAdmin)