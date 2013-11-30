# -*- coding: utf-8 -*-
import collections
from django.utils.translation import ugettext, ugettext_lazy as _
from django.db import models

class Map(models.Model):
    """
    The map model.
        -> name
        -> lines        
    """
    name = models.CharField(max_length=140, verbose_name=_('Name'),blank=False)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        url = 'map_view'
        return (url, [self.name])
    
    def get_lines(self):
        return Line.objects.filter(map=self)

class Line(models.Model):
    """
    The line model
        -> name
        -> color
        -> stops
    """    
    name = models.CharField(max_length=140, verbose_name=_('Name'),blank=False)
    map = models.ForeignKey(Map, related_name='stops')
    color = models.CharField(max_length=7, verbose_name=_('Color'),blank=False)
    stops = models.ManyToManyField('Stop', related_name='lines', blank=True, null=True,)
    
    def __unicode__(self):
            return self.name    
        
    def get_stops(self):
        return self.stops.all()
    
class Stop(models.Model):
    """
    The stop model
        ->name
        ->successors = dictionary of {Stop : Line}          
    """
    name = models.CharField(max_length=140, verbose_name=_('Name'),blank=False)
    column = models.CharField(max_length=4, verbose_name=_('Column'),blank=False)
    raw = models.CharField(max_length=4, verbose_name=_('Raw'),blank=False)
    
    def __unicode__(self):
        return self.name
    
    def get_successors(self):
        return Successor.objects.filter(stop=self)
    
class Successor(models.Model):
    """
    the successor model
        ->stop
        ->successor stop
        ->successor line
    """
    stop = models.ForeignKey(Stop)
    successor_stop = models.ForeignKey(Stop, related_name="Successor_Stop")
    successor_line = models.ForeignKey(Line, related_name="Successor_Line")
    
def create_subway(map_name, *lines, **system):
    """
    Given a list of lines & a system, create subway system consisting of :
        map, lines and stops
    """
    #create the map
    map, _ = Map.objects.get_or_create(name=map_name)    
    #create the lines
    lines_dict = {}    
    for l in lines[0]:
        linename, linecolor = l.split()
        line, _ = Line.objects.get_or_create(name=linename, map=map, color=linecolor)        
        lines_dict[linename] = line    
    #create stops
    #successors = collections.defaultdict(dict)
    for linename, stops in system.items():
        line = lines_dict[linename]   
        for stop1_str, stop2_str in overlaping_pairs(stops.split()):
            stop1_name, stop1_clm, stop1_raw = stop1_str.split('_')
            stop2_name, stop2_clm, stop2_raw = stop2_str.split('_')
            stop1, _ = Stop.objects.get_or_create(name=stop1_name, column=stop1_clm, raw=stop1_raw)
            stop2, _ = Stop.objects.get_or_create(name=stop2_name, column=stop2_clm, raw=stop2_raw)    
            line.stops.add(stop1)
            line.stops.add(stop2)                
            Successor.objects.get_or_create(stop = stop1, successor_stop=stop2, successor_line=line)
            Successor.objects.get_or_create(stop = stop2, successor_stop=stop1, successor_line=line)        
    
def overlaping_pairs(list):
    return [list[i:i+2] for i in range(len(list)-1)]
