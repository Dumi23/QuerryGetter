from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Airports, Destination, Flight


class FlightForm(ModelForm):
    destination = forms.ModelChoiceField(queryset=Destination.objects.all())
    airports = forms.ModelMultipleChoiceField(queryset=Airports.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Flight
        fields = ['name', 'destination', 'airports']


class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['name']

class AirportForm(ModelForm):
    class Meta:
        model = Airports
        fields = ['name']