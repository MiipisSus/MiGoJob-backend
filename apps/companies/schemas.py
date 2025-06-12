from ninja import ModelSchema
from typing import List

from .models import Company
from apps.jobs.schemas import JobSchema


class CompanySchema(ModelSchema):
    jobs: List[JobSchema]
    high_salary_jobs: List[JobSchema]
    average_salary: float
    
    @staticmethod
    def resolve_highest_salary_jobs(obj):
        return obj.jobs.filter(salary_min__gte=100000).order_by('-salary_min')
    
    class Meta:
        model = Company
        fields = '__all__'