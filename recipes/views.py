from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Uma linda string')


def sobre(request):
    return HttpResponse('contato')


def contato(request):
    return HttpResponse('sobre')
