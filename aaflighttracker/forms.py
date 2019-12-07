from django import forms

class searchform(forms.Form):
    flightorigin = forms.CharField(label="Flight Origin airport code", widget=forms.TextInput(attrs={'placeholder': 'lax', 'style': 'text-transform:lowercase;'}), max_length=3, min_length=3, required=True)        # Text input for Flight Origin
    flightdestination = forms.CharField(label="Flight Destination airport code", widget=forms.TextInput(attrs={'placeholder': 'dfw', 'style': 'text-transform:lowercase;'}), max_length=3, min_length=3, required=True)   # Text input for Flight destination
    flightdate = forms.DateField(label="Flight Date", widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}), required=True)           # Flight Date input format "2006-10-25'