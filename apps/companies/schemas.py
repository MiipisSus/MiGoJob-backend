from ninja import ModelSchema
from typing import List, Optional

from .models import Company
from apps.jobs.schemas import JobOut


class CompanyIn(ModelSchema):
    class Meta: 
        model = Company
        exclude = ['id', 'created_at', 'updated_at']

    
class CompanyOut(ModelSchema):
    jobs: List[JobOut] = []
    high_salary_jobs_count: int = 0
    average_salary: float
    
    @staticmethod
    def resolve_high_salary_jobs_count(obj):
        return obj.jobs.filter(salary_min__gte=100000).count()
    
    class Meta:
        model = Company
        fields = '__all__'
