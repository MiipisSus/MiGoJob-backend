from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from typing import List

from .schemas import UserIn, UserOut
from apps.common.shortcuts import update_object
from apps.auth import IsSuperuser, IsAuthenticated


router = Router(tags=['users'])

@router.get('/me', response=UserOut, auth=IsAuthenticated())
def retrieve_current_user(request):
    return request.auth

@router.put('/me', response=UserOut, auth=IsAuthenticated())
def update_current_user(request, payload: UserIn):
    user = request.auth
    user = update_object(instance=user, payload=payload)
    return user

@router.delete('/me', response={204: None}, auth=IsAuthenticated())
def delete_current_user(request):
    user = request.auth
    user.delete()
    return

@router.get('', response=List[UserOut], auth=IsSuperuser())
def list_users(request):
    users = User.objects.all().order_by('id')
    return users

@router.get('/{id}', response=UserOut, auth=IsSuperuser())
def retrieve_user(request, id: int):
    return get_object_or_404(User, id=id)

@router.post('', response={201: UserOut})
def create_user(request, payload: UserIn):
    user = User.objects.create_user(**payload.dict())
    return user

@router.put('/{id}', response=UserOut, auth=IsSuperuser())
def update_user(request, id: int, payload: UserIn):
    user = get_object_or_404(User, id=id)
    user = update_object(instance=user, payload=payload)
    return user

@router.delete('/{id}', response={204: None}, auth=IsSuperuser())
def delete_user(request, id: int):
    user = get_object_or_404(User, id=id)
    user.delete()
    return