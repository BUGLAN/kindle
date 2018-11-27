from django.db import models

# Create your models here.


class User(models.Model):
    nickname = models.CharField(max_length=30, null=True, verbose_name="用户名")
    personal_introduction = models.TextField(verbose_name="个人简介")
    password = models.CharField(max_length=35, null=True)
    email = models.EmailField(verbose_name="邮箱")
    profile_picture = models.ImageField(verbose_name="头像")


class Book(models.Model):
    """
    kindle book table
    """
    bookname = models.CharField(max_length=20, verbose_name="书名")
    book_introduction = models.TextField(verbose_name="简介")
    image = models.ImageField(verbose_name="图片")
    created_time = models.DateField(null=True, verbose_name="创建时间")
    published_time = models.DateField(null=True, verbose_name="修改时间")
    save_path = models.FilePathField("文件存储路径")