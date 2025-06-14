import factory
from factory.django import DjangoModelFactory
from pytest_factoryboy import register

from apps.companies.models import Company


@register
class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
        
    name = factory.Faker('company')
    description = factory.Faker('text')
