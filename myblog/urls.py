#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from myblog import views


app_name = 'myblog'
urlpatterns = [
    path('index/', views.index, name='index'),
]
