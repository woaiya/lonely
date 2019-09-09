#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myblog.models import GraphicRecordModels, LearnTypeModels, LabelModels, RecommendModels
from django.db.models.aggregates import Count


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
    view = GraphicRecordModels.objects.filter(graphic_state=1).order_by('-graphic_views')[:2]
    return view


def flip_over(graphic_id):
    """
    图文博客：上一篇下一篇处理
    """
    graphic_all = GraphicRecordModels.objects.exclude(graphic_state=0)
    if int(graphic_id) > 1:
        last_data = graphic_all.filter(graphic_id__lt=graphic_id).last()
    else:
        last_data = None
    if int(graphic_id) < graphic_all.count():
        next_data = graphic_all.filter(graphic_id__gt=graphic_id).first()
    else:
        next_data = None
    page = {
        "last": last_data,
        "next": next_data
    }
    return page


def label_list():
    """
    标签云
    """
    label_all = LabelModels.objects.filter(label_state=1).order_by('label_id')[:1]
    return label_all


def web_recommend():
    """
    站长推荐
    """
    recommend = RecommendModels.objects.filter(recommend_state=1).order_by('recommend_id')[:1]
    return recommend
