from django.db import models


class NuclearReactorConstructionProject(models.Model):
    ACTIVE = "active"
    COMPLETED = "completed"
    PROJECT_STATUS_CHOICES = {
        ACTIVE: "Active",
        COMPLETED: "Completed"
    }
    project_name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.IntegerField()
    project_site_boundaries = models.JSONField()
    project_status = models.CharField(max_length=10,choices= PROJECT_STATUS_CHOICES, default=ACTIVE) # active or completed
    project_phase = models.CharField(max_length=25) # design, permiting, construction, testing, licensing, operation
    estimated_construction_start_date = models.DateTimeField("estimated construction start date")
    construction_start_date = models.DateTimeField("construction start date")
    estimated_construction_completion_date = models.DateTimeField("estimated construction completion date")
    construction_completion_date = models.DateTimeField("construction completion date")
    estimated_cost = models.FloatField()
    total_expenses = models.FloatField()

    def is_active(self):
        return self.project_status == self.ACTIVE

    def is_completed(self):
        return self.project_status == self.COMPLETED

