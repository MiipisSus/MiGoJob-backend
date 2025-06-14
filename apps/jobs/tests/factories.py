import factory
from factory.django import DjangoModelFactory
from pytest_factoryboy import register

from apps.jobs.models import Job


@register
class JobFactory(DjangoModelFactory):
    class Meta:
        model = Job
        
    name = factory.Faker('job')
    company = factory.SubFactory('apps.companies.tests.factories.CompanyFactory')
    description = factory.Faker('text')
    salary_min = factory.Faker('random_int', min=30000, max=200000)
    salary_max = factory.Faker('random_int', min=30000, max=200000)
