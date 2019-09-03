from django.contrib import admin

# Register your models here.

from myblog.models import LearnTypeModels, LabelModels, AuthorModels, ArticleRecordModels, GraphicRecordModels


@admin.register(LearnTypeModels)
class LearnTypeAdmin(admin.ModelAdmin):
    list_display = ['learn_id', 'learn_name', 'category_colored_status']


@admin.register(LabelModels)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['label_id', 'label_name', 'category_colored_status']


@admin.register(AuthorModels)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'author_name', 'category_colored_status']


@admin.register(ArticleRecordModels)
class ArticleRecordAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'article_author', 'article_title', 'article_learn',
                    'article_views', 'category_colored_status']


@admin.register(GraphicRecordModels)
class GraphicRecordAdmin(admin.ModelAdmin):
    list_display = ['graphic_id', 'graphic_author', 'graphic_title', 'graphic_learn',
                    'graphic_views', 'category_colored_status']
