from django.shortcuts import render

# Create your views here.

from myblog.models import GraphicRecordModels, ArticleRecordModels, LearnTypeModels
from django.core.paginator import Paginator

from django.db.models.aggregates import Count


def index(request):
    """
    博客主页
    """
    graphic_data = Paginator(GraphicRecordModels.objects.filter(graphic_state=1).order_by('graphic_id'), 10)
    classify = article_classify()
    return render(request, 'myblog/index.html', {
        'posts': graphic_data.page(1),
        'classify': classify
    })


def mydiary(request):
    """
    文章博客主页，我的日记
    """
    article_data = Paginator(ArticleRecordModels.objects.filter(article_state=1).order_by('article_id'), 10)
    return render(request, 'myblog/list.html', {'posts': article_data.page(1)})


def graphic(request, graphic_id):
    """
    图文博客详情页
    """
    graphic_data = GraphicRecordModels.objects.get(graphic_id=graphic_id)
    graphic_all = GraphicRecordModels.objects.exclude(graphic_state=0)
    if int(graphic_id) > 1:
        last_data = graphic_all.filter(graphic_id__lt=graphic_id).last()
    else:
        last_data = None
    if int(graphic_id) < graphic_all.count():
        next_data = graphic_all.filter(graphic_id__gt=graphic_id).first()
    else:
        next_data = None
    classify = article_classify()
    view = view_ranking()
    return render(request, 'myblog/info.html', {
        'posts': graphic_data,
        'last': last_data,
        'next': next_data,
        'classify': classify,
        'views': view
    })


def article_classify():
    """
    文章分类
    """
    learn_num = LearnTypeModels.objects.filter(learn_state=1).annotate(num_articles=Count('graphicrecordmodels')).filter(num_articles__gt=0)
    return learn_num


def view_ranking():
    """
    浏览排行榜
    """
    view = GraphicRecordModels.objects.filter(graphic_state=1)[:2]
    return view
