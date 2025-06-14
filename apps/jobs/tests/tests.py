import pytest

@pytest.mark.django_db
class TestJobs:
    def test_companies_list(self, client):
        res = client.get('')
        assert res.status_code == 200
    
    def test_companies_retrieve(self, client, job):
        res = client.get(f'/{job.id}')
        assert res.status_code == 200
        
        res = client.get('/100')
        assert res.status_code == 404