from django.db import models
from django.contrib.auth.models import AbstractUser
from _datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='',blank=True)
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(blank=True,max_length=6, choices=(('male', '男'), ('female', '女')), default='female')
    addr = models.CharField(max_length=100, default='',blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(blank=True,upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register','注册'),('forget','找回密码')),max_length=10)
    send_time = models.DateField(default=datetime.now)
    def __str__(self):
        return self.code+'('+(self.email)+')'

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图',max_length=100)
    url = models.URLField(max_length=200,verbose_name='访问地址')
    index = models.IntegerField(verbose_name='顺序', default=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name