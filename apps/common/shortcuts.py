from django.db.models import Model
from ninja import Schema


def update_object(instance: Model, payload: Schema):
    for attr, value in payload.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance