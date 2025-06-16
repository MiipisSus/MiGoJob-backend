from django.test.client import Client
import pytest
from ninja_jwt.tokens import RefreshToken

from .factories import UserFactory
       

class JsonClient(Client):
    api_prefix = '/api'

    def _add_prefix(self, path):
        if not path.startswith(self.api_prefix):
            return f'{self.api_prefix}{path}'
        return path
    
    def get(self, path, data=None, content_type='application/json', **extra):
        return super().get(self._add_prefix(path), data, content_type, **extra)
    def post(self, path, data=None, content_type='application/json', **extra):
        return super().post(self._add_prefix(path), data, content_type, **extra)
    def put(self, path, data=None, content_type='application/json', **extra):
        return super().put(self._add_prefix(path), data, content_type, **extra)
    def patch(self, path, data=None, content_type='application/json', **extra):
        return super().patch(self._add_prefix(path), data, content_type, **extra)
    def delete(self, path, data=None, content_type='application/json', **extra):
        return super().delete(self._add_prefix(path), data, content_type, **extra)
    
    
@pytest.fixture(scope='session')
def client():
    client = JsonClient()
    return client

@pytest.fixture
def user_client(client: Client, user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    
    client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    return client

@pytest.fixture
def superuser_client(client: Client, user_factory):
    superuser = user_factory(is_superuser=True, is_staff=True)
    refresh = RefreshToken.for_user(superuser)
    access_token = str(refresh.access_token)
    
    client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    return client