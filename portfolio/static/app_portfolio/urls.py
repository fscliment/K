#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:28:31 2018

@author: fscliment
"""

from django.urls import path
from . import  views

urlpatterns = [
        
        path('',views.portfolio, name = "portfolio"),
        
        ]