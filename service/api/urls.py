from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NuclearReactorConstructionProjectViewSet, ContractorViewSet, ExpenditureViewSet, get_lat_lon
router = DefaultRouter()
router.register(r'projects', NuclearReactorConstructionProjectViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'expenditures', ExpenditureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get-lat-lon', get_lat_lon, name='get_lat_lon')
]