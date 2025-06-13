from ninja import Router
from ninja.errors import HttpError
from typing import List

from .models import Company
from .schemas import CompanySchema


router = Router(tags=['companies'])

@router.get('', response=List[CompanySchema])
def list_companies(request):
    companies = Company.objects.all()
    return companies

@router.get('/{id}', response=CompanySchema)
def retrieve_company(request, id: int):
    try:
        return Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise HttpError(404, f'Company with id {id} not found')
