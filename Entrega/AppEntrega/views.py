from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def inicio(request):   
    return HttpResponse(request, "AppEntrega/index.html")


