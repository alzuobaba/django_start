from django.db import models
from datetime import datetime
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=10)
    learn_times = models.IntegerField(verbose_name='学习时长', default=0)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    image = models.ImageField(verbose_name='封面图', upload_to='courses/%Y/%m', max_length=100)
    click_nums = models.IntegerField(verbose_name='点击数',default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间' )

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='章节名', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间' )

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='课程名', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间' )

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

class CourseResourse(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='资源名称', max_length=100)
    download = models.FileField(verbose_name='资源文件', max_length=100, upload_to='course/resource/%Y/%m')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name