from django.db import models
# from users.models import Organizational
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Organizational(models.Model):
    '''
    公司组织架构
    '''
    title=models.CharField(max_length=50,verbose_name='名称')
    parentid=models.CharField(max_length=64,verbose_name='钉钉父部门ID',null=True,blank=True)
    dingID=models.CharField(max_length=15,verbose_name='钉钉ID',null=True,blank=True)
    leader=models.ForeignKey(to=User,verbose_name='领导',null=True,
                            blank=True,help_text='部门领导',
                            on_delete=models.CASCADE)
    class Meta:
        verbose_name='部门名称'
    def __str__(self):return self.title

class Memu(models.Model):
    '''一级菜单'''
    title=models.CharField(verbose_name='菜单名称',max_length=30)
    icon=models.CharField(verbose_name='图标',null=True,blank=True,max_length=128)
    def __str__(self):return self.title


class Permission(models.Model):
    '''权限表'''
    title=models.CharField(verbose_name='标题',max_length=30)
    url=models.CharField(verbose_name='含正则的URL',max_length=256)
    # is_menu=models.BooleanField(verbose_name='是否菜单',default=False)
    # menu_title=models.CharField(verbose_name='菜单名称',null=True,blank=True,max_length=128)
    icon=models.CharField(verbose_name='图标',null=True,blank=True,max_length=128)
    memu=models.ForeignKey(to=Memu,verbose_name='所属一级菜单',
                           null=True,blank=True,help_text='',on_delete=models.CASCADE)
    pid = models.ForeignKey(to='Permission',verbose_name='权限所性二级菜单',null=True,
                            blank=True,help_text='不能成为二级菜单，但是要归属哪个二级菜单',
                            related_name='parents',on_delete=models.SET_NULL)
    def __str__(self):return self.title
class Role(models.Model):
    '''角色表'''
    title=models.CharField(verbose_name='标题',max_length=30)
    permission=models.ManyToManyField(verbose_name='权限',to=Permission,blank=True,help_text='修改后需要重新登录才能生效')
    user=models.ManyToManyField(to=User,verbose_name='包含用户',help_text='包含用户',blank=True)
    def __str__(self): return self.title

class UserInfo(models.Model):
    '''用户'''
    usertype=(
        ('0','系统注册用户'),
        ('1','钉钉用户'),
        ('2','微信用户'),

    ) #用户来源
    user=models.OneToOneField(to=User,verbose_name='用户',on_delete=models.CASCADE)
    role=models.ManyToManyField(verbose_name='权限',to=Role)
    organizational = models.ForeignKey(on_delete=models.CASCADE,to=Organizational, blank=True, verbose_name='部门')
    telphome = models.CharField(blank=True, max_length=15, null=True, verbose_name='电话')
    userSource=models.CharField(choices=usertype,verbose_name='用户来源',max_length=2,default='0')
    unionid=models.CharField(verbose_name='钉钉用户密码,unionid',max_length=64)
    openid=models.CharField(verbose_name='钉钉openid',max_length=64,null=True,blank=True)
    userid=models.CharField(verbose_name='钉钉dingId',max_length=64,default='0',help_text='userid该企业的唯一ID')
    position=models.CharField(verbose_name='职位信息',max_length=64,default='',help_text='职位信息',null=True)
    active=models.BooleanField(verbose_name='是否激活了钉钉',max_length=64,default=False,help_text='是否激活了钉钉')
    avatar=models.CharField(verbose_name='头像url',max_length=256,default='',help_text='钉钉头像url',null=True,blank=True)
    email=models.EmailField(verbose_name='email',max_length=256,null=True,blank=True,help_text='email')
    nick = models.CharField(blank=True, max_length=20, null=True,  verbose_name='昵称')
    name = models.CharField(blank=True, max_length=20, null=True, verbose_name='姓名')
    is_management=models.BooleanField(default=False,verbose_name='是否管理人员')
    is_active=models.BooleanField(default=True,verbose_name='活跃',help_text='False是禁止登录')



    class Meta:
        verbose_name = '用户表'

    def __str__(self):

        return self.name



