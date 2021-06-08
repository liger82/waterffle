from django.shortcuts import render
from django.views.generic import TemplateView

import logging

# settings.py 에서 설정한 logger를 취득
logger = logging.getLogger('waterffle_logger')

# Create your views here.
class PlaylistView(TemplateView):
    template_name = 'playlist.html'


