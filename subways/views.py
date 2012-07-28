# -*- coding: utf-8 -*-
'''
Created on Jav 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader
from subways.models import Map, Line, Stop
from subways.utilis import ride_path, longest_ride_path

def map(request, map_name, template_name=None):    
    """ view a map """
    map = Map.objects.get(name=map_name)
    lines = Line.objects.filter(map=map)
    stops = Stop.objects.all().values_list('name', flat=True)
    c = RequestContext(request, {'map': map,
                                 'lines': lines,  
                                 'stops': stops                               
                                 })
    return render_to_response(template_name, c)

def longest_ride(request, map_name, template_name=None):
    """"Return the longest possible (in terms of stops)
    ride between any two stops in the system."""
    map = Map.objects.get(name=map_name)
    lines = Line.objects.filter(map=map)
    stops = Stop.objects.all()
    path_stops = longest_ride_path(stops)
    stops = stops.values_list('name', flat=True)
    c = RequestContext(request, {'map': map,
                                 'lines': lines,
                                 'stops': stops,
                                 'path_stops': path_stops                                 
                                 })
    return render_to_response(template_name, c)

def ride(request, map_name, here='mit', there='government', template_name=None):
    """"Return the longest possible
    ride between any two stops in the system."""
    map = Map.objects.get(name=map_name)
    lines = Line.objects.filter(map=map)
    here_stop = Stop.objects.get(name=here)
    there_stop = Stop.objects.get(name=there)
    path_stops = ride_path(here_stop, there_stop)
    stops = Stop.objects.all().values_list('name', flat=True)
    c = RequestContext(request, {'map': map,
                                 'lines': lines,
                                 'stops': stops,  
                                 'path_stops': path_stops,                                 
                                 })
    return render_to_response(template_name, c)