from django.db import models

# Create your models here.
class Pc(models.Model):
    # PC
    title = models.CharField(max_length=50, verbose_name='计算机名称')
    code = models.CharField(max_length=2, verbose_name='大类物料代号')
    state = models.BooleanField(verbose_name='状态',default=True)
    class Meta:
        verbose_name='物料编码大类'
    def __str__(self):return self.title