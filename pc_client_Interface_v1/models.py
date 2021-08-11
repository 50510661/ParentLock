from django.db import models

# Create your models here.
class Pc_info(models.Model):
    # PC
    title = models.CharField(max_length=50, verbose_name='计算机名称')
    board_serialNumber = models.CharField(max_length=25, verbose_name='序列号')
    disk_serialNumber = models.CharField(max_length=500,null=True,blank=True,verbose_name='硬盘信息')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    change_add = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    class Meta:
        verbose_name='PC信息'
    def __str__(self):return self.title
class disk_info(models.Model):
    #硬盘信息
    serialNumber= models.CharField(max_length=25, verbose_name='序列号')
    pc= models.ForeignKey(to=Pc_info, verbose_name='电脑',on_delete=models.CASCADE)
    size=models.CharField(max_length=25, verbose_name='容量')
    _type=models.CharField(max_length=25,verbose_name='类型',null=True,blank=True,default='Mechanics')
    class Meta:
        verbose_name='硬盘信息'
    def __str__(self):return self.serialNumber
