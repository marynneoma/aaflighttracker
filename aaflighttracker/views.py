from django.shortcuts import render
import urllib.parse
import requests
from django.http import HttpResponse
from django import forms
from .forms import searchform

def flightviewer(request):
    return HttpResponse("Hello Mary Python Developer")