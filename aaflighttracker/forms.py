from django import forms

class searchform(forms.Form):
    flightorigin = forms.CharField(max_length=3, min_length=3, required=True)        # Text input for Flight Origin
    flightdestination = forms.CharField(max_length=3, min_length=3, required=True)   # Text input for Flight destination
    flightdate = forms.DateField(required=True)           # Flight Date input format "2006-10-25'