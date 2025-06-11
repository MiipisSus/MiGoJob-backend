from ninja import ModelSchema

from .models import Company

class CompanySchema(ModelSchema):
    class Meta:
        model = Company
        fields = '__all__'