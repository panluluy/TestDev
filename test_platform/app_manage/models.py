from django.db import models

# Create your models here.

# django的ORM
class Project(models.Model):
    """项目表"""
    name = models.CharField('名称',max_length=100,blank=False,default='')
    describe = models.TextField('描述',default='')
    status = models.BooleanField('状态',default=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)

class Module(models.Model):
    """模块表"""
    # 创建外键，使项目与模块关联，on_delete=models.CASCADE, 删除关联数据,与之关联也删除
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField('名称',max_length=100,null=False,default='')
    describe = models.TextField('描述',default='')
    update_time = models.DateTimeField('更新时间',auto_now=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    