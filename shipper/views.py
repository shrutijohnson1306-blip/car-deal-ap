from django.shortcuts import render
from django.http import HttpResponse
from .models import Shipper
from rest_framework import viewsets
from .serializers import ShipperSerializer

def shipper_list(request):
    shippers = Shipper.objects.all()
    if not shippers:
        return HttpResponse("No shippers found in the database")
    return render(request, 'shipper/shipper_list.html', {'shippers': shippers})

class ShipperViewSet(viewsets.ModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer