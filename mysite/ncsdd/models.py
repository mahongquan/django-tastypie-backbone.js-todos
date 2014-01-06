# -*- coding: utf-8 -*-
from django.db import models
import datetime
import logging
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
class Todo(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
