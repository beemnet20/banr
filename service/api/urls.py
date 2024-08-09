from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NuclearReactorConstructionProjectViewSet, ContractorViewSet, ExpenditureViewSet

router = DefaultRouter()
router.register(r'projects', NuclearReactorConstructionProjectViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'expenditures', ExpenditureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]