from ninja import NinjaAPI
from ninja.errors import ValidationError
from django.http import HttpResponse

from companies.api import router as companies_router
from jobs.api import router as jobs_router

api = NinjaAPI()

api.add_router('/companies/', companies_router)
api.add_router('/jobs/', jobs_router)