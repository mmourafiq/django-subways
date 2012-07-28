# -*- coding: utf-8 -*-
'''
Created on Jav 10, 2012

@author: Mourad Mourafiq

@copyright: Copyright © 2012

other contributers:
'''
from django.conf import settings
from django.utils.translation import ugettext_noop as _
from django.db.models import get_models, signals
from subways import models as subways

def create_system(app, created_models, verbosity, **kwargs):
    subways.create_subway('boston',
                          ('blue #4169E1', 'orange #FFA500', 'green #228B22', 'red #CD5C5C'),
                          blue='bowdoin_8_4 government_9_5 state_11_6 aquarium_12_7 maverick_13_6 airport_14_5 suffolk_14_5 revere_16_3 wonderland_19_1',
                          orange='oakgrove_12_1 sullivan_12_3 haymarket_13_5 state_11_6 downtown_10_7 chinatown_6_11 tufts_5_12 backbay_4_13 foresthills_1_15',
                          green='lechmere_8_1 science_9_1 north_9_2 haymarket_9_3 government_9_5 park_6_6 copley_5_7 kenmore_3_8 newton_2_8 riverside_1_8',
                          red='alewife_2_2 davis_3_2 porter_4_2 harvard_4_3 central_5_3 mit_5_4 charles_6_5 park_6_6 downtown_10_7 south_12_14 umass_14_15 mattapan_16_16')
                
signals.post_syncdb.connect(create_system, dispatch_uid=subways)
