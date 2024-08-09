from rest_framework import viewsets
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
