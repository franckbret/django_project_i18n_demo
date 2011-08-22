# -*- coding: utf-8 -*-
import os
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    from settings import *
except ImportError:
    pass

DEBUG = True
TEMPLATE_DEBUG = DEBUG