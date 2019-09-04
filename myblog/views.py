from django.shortcuts import render

# Create your views here.

from myblog.models import GraphicRecordModels
from django.core.paginator import Paginator


def index(request):
    """
    博客主页
    """
    graphic_data = Paginator(GraphicRecordModels.objects.filter(graphic_state=1).order_by('graphic_id'), 10)
    return render(request, 'myblog/index.html', {'posts': graphic_data.page(1)})


def graphic(request, graphic_id):
    """
    图文博客详情页
    """
    graphic_data = GraphicRecordModels.objects.get(graphic_id=graphic_id)
    graphic_all = GraphicRecordModels.objects.exclude(graphic_state=0)
    if int(graphic_id) > 1:
        # 上一篇 __lt 小于graphic_id  last()最后一个ID
        last_data = graphic_all.filter(graphic_id__lt=graphic_id).last()
    else:
        last_data = None
    if int(graphic_id) < graphic_all.count():
        # 上一篇 __gt 大于graphic_id  first()第一个ID
        next_data = graphic_all.filter(graphic_id__gt=graphic_id).first()
    else:
        next_data = None
    return render(request, 'myblog/info.html', {
        'posts': graphic_data,
        'last': last_data,
        'next': next_data
    })
