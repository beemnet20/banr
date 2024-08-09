from django.contrib import admin
from .models import NuclearReactorConstructionProject, Contractor, Expenditure

@admin.register(NuclearReactorConstructionProject)
class NuclearReactorConstructionProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_status', 'project_phase']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['company_name','field_of_work','contact_person','phone_number','email']

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['expense_name', 'amount', 'contractor', 'project', 'date_incurred']
