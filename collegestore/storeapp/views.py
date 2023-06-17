from django.shortcuts import render, redirect
from django.template.context_processors import request


def home(request):
    return render(request,"home.html")



