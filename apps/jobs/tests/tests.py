import pytest

@pytest.mark.django_db
class TestJobs:
    def test_jobs_list(self, client):
        res = client.get('/jobs')
        assert res.status_code == 200
    
    def test_jobs_retrieve(self, client, job):
        res = client.get('/jobs/' + f'{job.id}')
        assert res.status_code == 200
        
        res = client.get('/jobs/100')
        assert res.status_code == 404
        
    def test_jobs_create_success(self, superuser_client, company):
        data = {
            'name': 'Test Job',
            'company_id': company.id,
            'description': 'This is a test job description.',
            'salary_min': 50000,
            'salary_max': 100000,
        }
        
        res = superuser_client.post('/jobs', data=data)
        assert res.status_code == 201
        assert res.json()['name'] == data['name']
        
    def test_jobs_create_failure(self, user_client, company):
        data = {
            'name': 'Test Job',
            'company_id': company.id,
            'description': 'This is a test job description.',
            'salary_min': 50000,
            'salary_max': 100000,
        }
        
        res = user_client.post('/jobs', data=data)
        assert res.status_code == 403
    
    def test_jobs_update_success(self, superuser_client, job):
        data = {
            'name': 'Updated Job',
            'company_id': job.company.id,
            'description': 'This is an updated job description.',
            'salary_min': 60000,
            'salary_max': 120000,
        }
        
        res = superuser_client.put(f'/jobs/{job.id}', data=data)
        assert res.status_code == 200
        assert res.json()['name'] == data['name']
    
    def test_jobs_update_failure(self, superuser_client, job):
        data = {
            'name': 'Updated Job',
            'company_id': 100,  # Invalid company ID
            'description': 'This is an updated job description.',
            'salary_min': 60000,
            'salary_max': 120000,
        }
        res = superuser_client.put(f'/jobs/{job.id}', data=data)
        assert res.status_code == 404
        
    def test_jobs_delete(self, superuser_client, job):
        res = superuser_client.delete(f'/jobs/{job.id}')
        assert res.status_code == 204
    