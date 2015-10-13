#!/usr/bin/env python
import sys,os,time
#import tri_config,tri_module
sys.path.append('/home/limian/py_web')
os.environ['DJANGO_SETTINGS_MODULE'] ='py_web.settings'
#----------------Use Django Mysql model----------------
from web.models import * 
