from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
import pgeocode
from .models import NuclearReactorConstructionProject, Contractor, Expenditure
from .serializers import NuclearReactorConstructionProjectSerializer, ContractorSerializer, ExpenditureSerializer

class NuclearReactorConstructionProjectViewSet(viewsets.ModelViewSet):
    queryset = NuclearReactorConstructionProject.objects.all()
    serializer_class = NuclearReactorConstructionProjectSerializer

class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer


@api_view(['GET'])
def get_lat_lon(request):
    zipcode = request.GET.get('zipcode', None)

    if not zipcode:
        return JsonResponse({'error': 'Zipcode is required'}, status=400)

    nomi = pgeocode.Nominatim('us')
    location = nomi.query_postal_code(zipcode)

    if location.latitude is None or location.longitude is None:
        return JsonResponse({'error': 'Invalid zipcode'}, status=400)

    return JsonResponse({
        'zipcode': zipcode,
        'latitude': location.latitude,
        'longitude': location.longitude
    })