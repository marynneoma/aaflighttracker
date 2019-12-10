from django.shortcuts import render
import urllib.parse
import requests
from django.http import HttpResponse
from django import forms
from .forms import searchform

def flightviewer(request): # defining all variables
    apiurl = 'https://american-flight-engine-2019.herokuapp.com/flights?date='
    origin = '&origin='
    destination = '&destination='
    htmltemplate = 'aaflighttracker/index.html'

    if request.method == 'POST': # if user fill out the form and post
        flightform = searchform(request.POST)
        if flightform.is_valid():
            flightorigin = flightform.cleaned_data['flightorigin']
            flightdestination = flightform.cleaned_data['flightdestination']
            flightdate = str(flightform.cleaned_data['flightdate'])
            fullurl = apiurl + flightdate + origin + flightorigin + destination + flightdestination
            jsondata = requests.get(fullurl).json()
            args = {                    
                'form': flightform,
                'jsondata': jsondata,
                'recordcount': len(jsondata),
                'fullurl': fullurl,
                'message': "Available Flights Shown Below"
            }
            return render(request, htmltemplate, args)
        else:                                                           # if reguest do not post
            flightform = searchform()
            args = {
                'form': flightform,
                'message': "The Form Entries are invalid"
            }
            return render(request, htmltemplate, args)
    else:                                               # if user is new to the page
        flightform = searchform()
        args = {
            'form': flightform,
            'message': "Fill the form to search for a flight"
        }
        return render(request, htmltemplate, args)