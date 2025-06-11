from ninja import ModelSchema

from .models import Company

class CompanySchema(ModelSchema):
    average_salary: float
    
    class Meta:
        model = Company
        fields = '__all__'