from django.db import models


class Job(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='jobs')
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'jobs'