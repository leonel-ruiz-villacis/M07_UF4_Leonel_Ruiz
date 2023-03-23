
from django.shortcuts import render

def header(request):
    return render(request, 'header/header.html')

