from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    '''
    Django 要求模型必须继承models.Model类
    Category 只需要一个简单的分类名name就可以了
    CharField 指定了分类名 name 的数据类型,CharField是字符型
    CharField 的max_length 参数指定其最大长度,超过这个长度的分类名就不能被存入数据库
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类 和分类表建立外键
    category = models.ForeignKey(Category)
    # 标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 自定义get_absolute_url 方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})