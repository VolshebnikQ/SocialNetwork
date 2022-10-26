from django.shortcuts import render
from django.views.generic import View

from .models import *


class Index(View):
    """Главная страница"""
    def get(self, request, *args, **kwargs):
        return render(request, 'index/index.html')
