from django.shortcuts import render

from models.forms import AirportForm, DestinationForm, FlightForm
from .models import Airports, Destination, Flight

# Create your views here.
def flight(request, pk):
    flight = Flight.objects.get(pk=pk)
    airports = flight.airports.all()
    return render(request, 'flight.html', {'flight': flight, 'airports': airports})

def create_flight(request):
    form = FlightForm()
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'flight_create.html', context)


def create_destination(request):
    form = DestinationForm()
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'destination_create.html', context)


def create_airport(request):
    form = AirportForm()
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'airport_create.html', context)
