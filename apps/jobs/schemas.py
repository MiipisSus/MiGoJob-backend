from .models import Job
from ninja import ModelSchema

        
class JobIn(ModelSchema):
    company_id: int
    
    class Meta:
        model = Job
        exclude = ['id', 'company', 'created_at', 'updated_at']
        
class JobOut(ModelSchema):
    company_id: int
    company_name: str
    
    class Meta:
        model = Job
        exclude = ['company', 'created_at', 'updated_at']

    @staticmethod
    def resolve_company_id(obj):
        return obj.company.id
    
    @staticmethod
    def resolve_company_name(obj):
        return obj.company.name
    