from django.core.management.base import BaseCommand, CommandError
from apps.jobs.models import Job
from apps.companies.models import Company

from faker import Faker

fake = Faker('zh_TW')

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            type=int,
            default=10,
            help='Number of companies to create (default: 10)'
        )
        parser.add_argument(
            '-j',
            type=int,
            default=10,
            help='Number of jobs per company to create (default: 10)'
        )
        
    def handle(self, *args, **options):
        num_companies = options['c']
        num_jobs = options['j']
        
        for _ in range(num_companies):
            company = Company.objects.create(
                name=fake.company(),
                description=fake.text()
            )
            for _ in range(num_jobs):
                salary_min, salary_max = sorted([fake.random_int(min=30000, max=200000) for _ in range(2)])
                Job.objects.create(
                    name=fake.job(),
                    description=fake.text(),
                    salary_min=salary_min,
                    salary_max=salary_max,
                    company=company
                )
        
        print("Database seeded with fake data")