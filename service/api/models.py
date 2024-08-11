from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Contractor(models.Model):
    company_name = models.CharField(max_length=50, null=False)
    field_of_work = models.CharField(max_length=50, null = True)
    contact_person = models.CharField(max_length=50, null = True)
    phone_number = models.CharField(max_length=12, null = True)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Contractor"
        verbose_name_plural = "Contractors"


class Expenditure(models.Model):
    MATERIALS = 'materials'
    LABOR = 'labor'
    EQUIPMENT = 'equipment'
    OTHER = 'other'
    CATEGORY_CHOICES = [
        (MATERIALS, 'Materials'),
        (LABOR, 'Labor'),
        (EQUIPMENT, 'Equipment'),
        (OTHER, 'Other'),
    ]
    expense_name = models.CharField(max_length=100, null=False)
    amount = models.FloatField(null=False)
    date_incurred = models.DateField(null=True)
    description = models.TextField(null=True)
    project = models.ForeignKey(
        'NuclearReactorConstructionProject',
        related_name='expenditures',
        on_delete=models.CASCADE
    )
    contractor = models.ForeignKey(
        'Contractor',
        related_name='expenditures',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=OTHER,
        null=True
    )

    def __str__(self):
        return f"{self.expense_name} - ${self.amount:.2f}"

    class Meta:
        verbose_name = "Expenditure"
        verbose_name_plural = "Expenditures"
        ordering = ['date_incurred']


class NuclearReactorConstructionProject(models.Model):
    ACTIVE = "active"
    COMPLETED = "completed"
    PROJECT_STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
    )

    DESIGN = "design"
    DESIGN_REVIEW = "design review"
    DESIGN_APPROVAL = "design approval"
    CONSTRUCTION = "construction"
    TESTING = "testing"
    REGULATORY_REVIEW = "regulatory review"
    OPERATIONAL = "operational"
    PROJECT_PHASE_CHOICES = (
        (DESIGN, "Design"),
        (DESIGN_REVIEW, "Design Review"),
        (DESIGN_APPROVAL, "Design Approval"),
        (CONSTRUCTION, "Construction"),
        (TESTING, "Testing"),
        (REGULATORY_REVIEW, "Regulatory Review"),
        (OPERATIONAL, "Operational"),
    )
    project_name = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=True)
    state = models.CharField(max_length=25, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    project_site_boundaries = models.JSONField(null=True)
    project_status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES,
                                      default=ACTIVE, null=True)
    project_phase = models.CharField(max_length=25, choices=PROJECT_PHASE_CHOICES, default = DESIGN, null=True)
    estimated_construction_start_date = models.DateField("estimated construction start date")
    construction_start_date = models.DateField("construction start date", null=True)
    estimated_construction_completion_date = models.DateField("estimated construction completion date", null=True)
    construction_completion_date = models.DateField("construction completion date", null = True)
    estimated_cost = models.FloatField(default=0.0, null=True)
    budget = models.FloatField(default=0.0, null=True)
    total_expenses = models.FloatField(default=0.0, null=True)
    contractors = models.ManyToManyField('Contractor', related_name="projects")
    power_rating_gw = models.IntegerField(default=1, null=True)
    notes = models.TextField(null=True)

    def is_active(self):
        return self.project_status == self.ACTIVE

    def is_completed(self):
        return self.project_status == self.COMPLETED

    def mark_project_completed(self):
        self.project_status = self.ACTIVE
        self.save()

    def update_total_expenses(self):
        self.total_expenses = self.expenditures.aggregate(models.Sum('amount'))['amount__sum'] or 0.0
        self.save()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Nuclear Reactor Construction Project"
        verbose_name_plural = "Nuclear Reactor Construction Projects"


@receiver(post_save, sender=Expenditure)
@receiver(post_delete, sender=Expenditure)
def update_project_total_expenses(sender, instance, **kwargs):
    instance.project.update_total_expenses()
