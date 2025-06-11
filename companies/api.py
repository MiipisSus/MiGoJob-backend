from ninja import Router
from ninja.errors import HttpError
from typing import List

from .models import Company
from .schemas import CompanySchema


router = Router()

@router.get('/companies', response=List[CompanySchema])
def list_companies(request):
    return Company.objects.all()

@router.get('/companies/{id}', response=CompanySchema)
def retrieve_company(request, id: int):
    try:
        return Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise HttpError(404, f'Company with id {id} not found')
