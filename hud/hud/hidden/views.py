from .zhelezko import eating
from django.shortcuts import render


def about(request):
    return render(request,'index.html', {'data': eating()})
