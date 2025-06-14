import pytest

@pytest.mark.django_db
class TestCompanies:
    def test_companies_list(self, client):
        res = client.get('')
        assert res.status_code == 200
    
    def test_companies_retrieve(self, client, company):
        res = client.get(f'/{company.id}')
        assert res.status_code == 200
        
        res = client.get('/100')
        assert res.status_code == 404