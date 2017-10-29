from django.db import models


# Create your models here.
class bookinfo(models.Model):
    btitle = models.CharField(verbose_name="图书",max_length=20)  # 图书 的名字
    bpub_date = models.DateField(verbose_name="发布时间",auto_now=True)  # 发布日期
    bread = models.IntegerField(verbose_name="阅读量",default=0)  # 阅读量
    bcomment = models.IntegerField(verbose_name="评论量",default=0)  # 评论量
    isDelete = models.BooleanField(verbose_name="是否删除",default=False)  # 逻辑删除

    def __str__(self):
        return self.btitle
    # def name(self):  # 改变标题的名字
    #     return self.btitle

class heroinfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄名字
    hgender = models.BooleanField(default=True)  # 熊熊的性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcomment = models.CharField(max_length=200)  # 描述信息
    hbook = models.ForeignKey('bookinfo')  # 外键 与图书一对多,

    # hbook = models.ForeignKey("关联的类名")  一对多
    # hbook = models.ManyToManyField("lei ming") 多对多
    # hbook = models.OneToOneField("类名") 一对一
    def __str__(self):
        return self.hname
    def gongfu(self):
        return self.hcomment
    def hname1(self):
            return self.hname
    def hgender1(self):
            return self.hgender
    def hbook1(self):
            return self.hbook
    gongfu.admin_order_field="hcomment"
    gongfu.short_description="功夫"
    hname1.admin_order_field="hname"
    hname1.short_description="名字"
    hgender1.admin_order_field="hgender"
    hgender1.short_description="男/女"
    hbook1.admin_order_field="hbook"
    hbook1.short_description="对应图书"



class yuan(models.Model):
    class Meta:
        db_table = "bing"


class HostGroup(models.Model):
    hgid = models.AutoField(primary_key=True)
    host_id = models.ForeignKey('Host')
    group_id = models.ForeignKey('Group')


# 一对多
class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)


class Group(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    # 指定第三张表
    h2g = models.ManyToManyField('Host', through='HostGroup')


class h1(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)


class h2(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    # 任意一个字段，会自动生成第三张表，且第三张表会自动的添加联合唯一索引，Unique
    h2g = models.ManyToManyField('h1')


class PicTest(models.Model):
    # 创建包含图片路径的模型类
    pic = models.ImageField(upload_to="book_app/")
    # 记录我闷提交图片的位置
