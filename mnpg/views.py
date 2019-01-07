from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template

from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def home(request):
    return render(request, 'mnpg/home.html')

def about(request):
    return render(request, 'mnpg/about.html')

def cv(request):
    return render(request, 'mnpg/cv.html')

