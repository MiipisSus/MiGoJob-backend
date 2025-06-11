from ninja import Router
from ninja.errors import HttpError
from typing import List

from .models import Job
from .schemas import JobSchema


router = Router()

@router.get('/jobs', response=List[JobSchema])
def list_jobs(request):
    return Job.objects.all()

@router.get('/jobs/{id}', response=JobSchema)
def retrieve_job(request, id: int):
    try:
        return Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise HttpError(404, f'Job with id {id} not found')