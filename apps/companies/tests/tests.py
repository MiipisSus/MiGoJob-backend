import pytest

@pytest.mark.django_db
class TestCompanies:
    def test_companies_list(self, client):
        res = client.get('/companies')
        assert res.status_code == 200
    
    def test_companies_retrieve(self, client, company):
        res = client.get(f'/companies/{company.id}')
        assert res.status_code == 200
        
        res = client.get('/companies/100')
        assert res.status_code == 404
        
    def test_companies_create(self, superuser_client):
        data = {
            'name': 'Test Company',
            'description': 'This is a test company description.',
        }
        
        res = superuser_client.post('/companies', data=data)
        assert res.status_code == 201
        assert res.json()['name'] == data['name']
        
    def test_companies_update(self, superuser_client, company):
        data = {
            'name': 'Updated Company',
            'description': 'This is an updated company description.',
        }
        
        res = superuser_client.put(f'/companies/{company.id}', data=data)
        assert res.status_code == 200
        assert res.json()['name'] == data['name']
        
    def test_companies_delete(self, superuser_client, company):
        res = superuser_client.delete(f'/companies/{company.id}')
        assert res.status_code == 204