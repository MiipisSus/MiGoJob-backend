from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List

from .models import Company
from .schemas import CompanyIn, CompanyOut
from apps.common.shortcuts import update_object
from apps.auth import IsAuthenticated, IsSuperuser


router = Router(tags=['companies'])

@router.get('', response=List[CompanyOut])
def list_companies(request):
    companies = Company.objects.all().order_by('-created_at')
    return companies

@router.get('/{id}', response=CompanyOut)
def retrieve_company(request, id: int):
    return get_object_or_404(Company, id=id)

@router.post('', response={201: CompanyOut}, auth=IsSuperuser())
def create_company(request, payload: CompanyIn):
    company = Company.objects.create(**payload.dict())
    return company

@router.patch('/{id}', response=CompanyOut, auth=IsSuperuser())
def update_company(request, id: int, payload: CompanyIn):
    company = get_object_or_404(Company, id=id)
    company = update_object(instance=company, payload=payload)
    return company

@router.delete('/{id}', response={204: None}, auth=IsSuperuser())
def delete_company(request, id: int):
    company = get_object_or_404(Company, id=id)
    company.delete()
    return