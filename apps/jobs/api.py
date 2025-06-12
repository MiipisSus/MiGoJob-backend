from ninja import Router
from ninja.errors import HttpError
from typing import List

from .models import Job
from .schemas import JobSchema, JobResponseSchema


router = Router(tags=['jobs'])

@router.get('', response=List[JobResponseSchema])
def list_jobs(request, keyword: str = None):
    return Job.objects.filter(name__contains=keyword) if keyword else Job.objects.all()

@router.get('/{id}', response=JobResponseSchema)
def retrieve_job(request, id: int):
    try:
        return Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise HttpError(404, f'Job with id {id} not found')