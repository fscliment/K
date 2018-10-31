#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:46:10 2018

@author: fscliment
"""
from django.urls import path

from . import views

urlpatterns = [
        
               path('blog/',views.post_list, name ="post_list"),
               path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
               
              ]