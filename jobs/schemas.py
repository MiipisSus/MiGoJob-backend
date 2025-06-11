from .models import Job
from ninja import ModelSchema

class JobSchema(ModelSchema):
    class Meta:
        model = Job
        fields = '__all__'