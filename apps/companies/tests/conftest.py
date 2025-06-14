import pytest
from ninja.testing import TestClient

from apps.companies.api import router
from apps.tests.factories import *

@pytest.fixture(scope='session')
def client():
    return TestClient(router)