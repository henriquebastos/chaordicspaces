# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'core/home.html')

@login_required
def subscription_new(request):
    return render(request, 'core/subscription_new.html', {
        'MOIP_TOKEN': settings.MOIP_TOKEN,
        'MOIP_PLAN': settings.MOIP_PLAN,
        'MOIP_URL': settings.MOIP_URL,
    })
