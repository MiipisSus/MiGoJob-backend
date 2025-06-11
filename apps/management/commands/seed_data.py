from django.core.management.base import BaseCommand, CommandError
from apps.jobs.models import Job
from apps.companies.models import Company

from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **options):
        for _ in range(3):
            company = Company.objects.create(
                name=fake.company()
            )
            for _ in range(5):
                salary_min, salary_max = sorted([fake.random_int(min=1000, max=10000) / 100 for _ in range(2)])
                Job.objects.create(
                    name=fake.job(),
                    description=fake.text(),
                    salary_min=salary_min,
                    salary_max=salary_max,
                    company=company
                )
        
        print("Database seeded with fake data")