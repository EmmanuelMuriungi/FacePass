# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Records
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    records = Records.objects.all()[:10]    
    context = {
        'records': records
    }
    return render(request, 'records.html', context)

def details(request, id):
    record = Records.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'details.html', context)
