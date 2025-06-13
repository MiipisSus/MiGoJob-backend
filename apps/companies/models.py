from django.db import models
from django.db.models import F, ExpressionWrapper


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    
    @property
    def average_salary(self):
        jobs = self.jobs.annotate(
            midpoint=ExpressionWrapper((F('salary_min') + F('salary_max')) / 2, output_field=models.FloatField())
        )
        avg = jobs.aggregate(avg=models.Avg('midpoint'))['avg']
        return round(avg, 2) if avg is not None else 0
    
    class Meta:
        db_table = 'companies'