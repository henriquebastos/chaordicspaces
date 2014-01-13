# coding: utf-8
from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')

def subscription_new(request):
    return render(request, 'core/subscription_new.html', {
        'MOIP_TOKEN': settings.MOIP_TOKEN,
        'MOIP_PLAN': settings.MOIP_PLAN,
    })
