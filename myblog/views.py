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
    return render(request, 'myblog/info.html', {'posts': graphic_data})
