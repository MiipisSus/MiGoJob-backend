from .models import Job
from ninja import ModelSchema


class JobSchema(ModelSchema):
    company_id: int
    
    @staticmethod
    def resolve_company_id(obj):
        return obj.company.id
    
    class Meta:
        model = Job
        exclude = ['company']
        
class JobResponseSchema(JobSchema):
    company_name: str
    
    @staticmethod
    def resolve_company_name(obj):
        return obj.company.name