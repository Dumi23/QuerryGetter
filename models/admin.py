from django.contrib import admin
from .models import Flight, Destination, Airports

# Register your models here.
admin.site.register(Flight)
admin.site.register(Destination)
admin.site.register(Airports)