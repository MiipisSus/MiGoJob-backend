from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404

from apps.jobs.models import Job
from apps.companies.models import Company
from .schemas import JobIn, JobOut
from apps.common.shortcuts import update_object
from apps.auth import IsSuperuser

router = Router(tags=['jobs'])

@router.get('', response=List[JobOut])
def list_jobs(request, keyword: str = None):
    jobs = Job.objects.filter(name__contains=keyword) if keyword else Job.objects.all()
    return jobs.order_by('-created_at')

@router.get('/{id}', response=JobOut)
def retrieve_job(request, id: int):
    return get_object_or_404(Job, id=id)
    
@router.post('', response=JobOut, auth=IsSuperuser())
def create_job(request, payload: JobIn):
    get_object_or_404(Company, id=payload.company_id)
    
    job = Job.objects.create(**payload.dict())
    return job

@router.patch('/{id}', response=JobOut, auth=IsSuperuser())
def update_job(request, id: int, payload: JobIn):
    get_object_or_404(Company, id=payload.company_id)
    
    job = get_object_or_404(Job, id=id)
    job = update_object(instance=job, payload=payload)
    
    return job

@router.delete('/{id}', auth=IsSuperuser())
def delete_job(request, id: int):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return