from rest_framework import serializers
from .models import NuclearReactorConstructionProject, Contractor, Expenditure


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class ExpenditureSerializer(serializers.ModelSerializer):
    contractor = ContractorSerializer(read_only=True)

    class Meta:
        model = Expenditure
        fields = '__all__'


class NuclearReactorConstructionProjectSerializer(serializers.ModelSerializer):
    expenditures = ExpenditureSerializer(many=True, read_only=True)

    class Meta:
        model = NuclearReactorConstructionProject
        fields = '__all__'
