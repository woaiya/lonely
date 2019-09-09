from django.shortcuts import render

# Create your views here.

from myblog.models import GraphicRecordModels, ArticleRecordModels
from django.core.paginator import Paginator

from myblog import basis


def index(request):
    """
    博客主页
    """
    graphic_data = Paginator(GraphicRecordModels.objects.filter(graphic_state=1).order_by('graphic_id'), 10)
    classify = basis.article_classify()
    recommend = basis.web_recommend()
    return render(request, 'myblog/index.html', {
        'posts': graphic_data.page(1),
        'classify': classify,
        'recommends': recommend
    })


def mydiary(request):
    """
    文章博客主页，我的日记
    """
    article_data = Paginator(ArticleRecordModels.objects.filter(article_state=1).order_by('article_id'), 10)
    classify = basis.article_classify()
    view = basis.view_ranking()
    label = basis.label_list()
    recommend = basis.web_recommend()
    return render(request, 'myblog/list.html', {
        'posts': article_data.page(1),
        'classify': classify,
        'views': view,
        'labels': label,
        'recommends': recommend
    })


def graphic(request, graphic_id):
    """
    图文博客详情页
    """
    graphic_data = GraphicRecordModels.objects.get(graphic_id=graphic_id)
    page = basis.flip_over(graphic_id)
    classify = basis.article_classify()
    view = basis.view_ranking()
    label = basis.label_list()
    recommend = basis.web_recommend()
    GraphicRecordModels.objects.filter(graphic_id=graphic_id).update(graphic_views=graphic_data.graphic_views + 1)
    return render(request, 'myblog/info.html', {
        'posts': graphic_data,
        'last': page['last'],
        'next': page['next'],
        'classify': classify,
        'views': view,
        'labels': label,
        'recommends': recommend
    })
