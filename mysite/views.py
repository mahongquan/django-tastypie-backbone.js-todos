# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
def index(request):
    return HttpResponseRedirect("/static/backbone_todos/index.html")
