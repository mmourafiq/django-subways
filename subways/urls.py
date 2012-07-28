# -*- coding: utf-8 -*-
'''
Created on Jav 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django.conf.urls import patterns, include, url 
from subways import views as subways

urlpatterns = patterns('', 
    url(r'^(?P<map_name>[\w.]+)/$', subways.map, {'template_name': "subways/subwayMap.htm"}, name='subway_map'),
    url(r'^longest_ride/(?P<map_name>[\w.]+)/$', subways.longest_ride, {'template_name': "subways/subwayMap.htm"}, name='subway_longest_ride'),
    url(r'^ride/(?P<map_name>[\w.]+)/(?P<here>[\w.]+)/(?P<there>[\w.]+)/$', subways.ride, {'template_name': "subways/subwayMap.htm"}, name='subway_ride'),   
    )