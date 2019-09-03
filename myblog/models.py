from django.db import models

# Create your models here.

from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from system.storage import ImageStorage


class LearnTypeModels(models.Model):

    """
    博客中学习的类型表
    learn_extend 为扩展字段，暂未使用
    """

    learn_id = models.AutoField(primary_key=True)
    learn_name = models.CharField(null=False, max_length=20, verbose_name='类型名')
    learn_extend = models.CharField(null=True, max_length=150, verbose_name='扩展字段')
    learn_state = models.IntegerField(default=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.learn_state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.learn_name

    class Meta:
        db_table = 'learn'
        verbose_name = '学习类型'
        verbose_name_plural = verbose_name


class LabelModels(models.Model):

    """
    博客中的标签表
    """

    label_id = models.AutoField(primary_key=True)
    label_name = models.CharField(null=False, max_length=20, verbose_name='类型名')
    label_extend = models.CharField(null=True, max_length=150, verbose_name='扩展字段')
    label_state = models.IntegerField(default=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.label_state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.label_name

    class Meta:
        db_table = 'label'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class AuthorModels(models.Model):

    """
    博客中的作者表
    """

    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(null=False, max_length=20, verbose_name='类型名')
    author_extend = models.CharField(null=True, max_length=150, verbose_name='扩展字段')
    author_state = models.IntegerField(default=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.author_state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class ArticleRecordModels(models.Model):

    """
    纯文字的博客
    """

    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=150, verbose_name='标题')
    article_body = RichTextField(verbose_name='内容')
    article_state = models.IntegerField(default=1, verbose_name='状态')
    article_learn = models.ForeignKey(LearnTypeModels, default=1, on_delete=models.DO_NOTHING, verbose_name='分类')
    article_views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    article_cover = models.ImageField(upload_to='images/%Y/%m/%d', storage=ImageStorage(), max_length=255, verbose_name='封面')
    article_about = models.CharField(max_length=100, verbose_name='简介')
    article_author = models.ForeignKey(AuthorModels, default=1, on_delete=models.DO_NOTHING, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.article_state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.article_title

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class GraphicRecordModels(models.Model):

    """
    图文的博客
    """
    graphic_id = models.AutoField(primary_key=True)
    graphic_title = models.CharField(max_length=150, verbose_name='标题')
    graphic_body = RichTextUploadingField(config_name='default', verbose_name='内容')
    graphic_state = models.IntegerField(default=1, verbose_name='状态')
    graphic_learn = models.ForeignKey(LearnTypeModels, default=1, on_delete=models.DO_NOTHING, verbose_name='分类')
    graphic_views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    graphic_cover = models.ImageField(upload_to='images/%Y/%m/%d', storage=ImageStorage(), max_length=255, verbose_name='封面')
    graphic_about = models.CharField(max_length=100, verbose_name='简介')
    graphic_author = models.ForeignKey(AuthorModels, default=1, on_delete=models.DO_NOTHING, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.graphic_state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.graphic_title

    class Meta:
        db_table = 'graphic'
        verbose_name = '图文'
        verbose_name_plural = verbose_name
