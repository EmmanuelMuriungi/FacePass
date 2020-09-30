# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    program = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)    
    fees_cleared = models.CharField(max_length=150, null=True)
    recorded_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = "Records"
