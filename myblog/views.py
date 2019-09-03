from django.shortcuts import render

# Create your views here.

from myblog.models import GraphicRecordModels
from django.core.paginator import Paginator


def index(request):
    graphic = GraphicRecordModels.objects.filter(graphic_state=1).order_by('graphic_id')
    graphic_data = Paginator(graphic, 10)
    return render(request, 'myblog/index.html', {'posts': graphic_data.page(1)})
