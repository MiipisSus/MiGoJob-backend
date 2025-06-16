import pytest


class TestUsers:
    @pytest.mark.django_db
    def test_users_list(self, superuser_client):
        res = superuser_client.get('/users')
        assert res.status_code == 200

    @pytest.mark.django_db
    def test_users_retrieve(self, superuser_client, user):
        res = superuser_client.get(f'/users/{user.id}')
        assert res.status_code == 200
        
        res = superuser_client.get('/users/100')
        assert res.status_code == 404
        
    @pytest.mark.django_db
    def test_users_create(self, client):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        res = client.post('/users', data=data)
        assert res.status_code == 201
        assert res.json()['username'] == data['username']
        
    @pytest.mark.django_db
    def test_users_update(self, superuser_client, user):
        data = {
            'username': 'updateduser',
            'password': 'updatedpassword',
            'email': ''
        }
        
        res = superuser_client.put(f'/users/{user.id}', data=data)
        assert res.status_code == 200
        assert res.json()['username'] == data['username']
        
    @pytest.mark.django_db
    def test_users_delete(self, superuser_client, user):
        res = superuser_client.delete(f'/users/{user.id}')
        assert res.status_code == 204
        
    @pytest.mark.django_db
    def test_users_me_retrieve(self, user_client, user):
        res = user_client.get('/users/me')
        assert res.status_code == 200
        assert res.json()['id'] == user.id
    
    @pytest.mark.django_db
    def test_users_me_update(self, user_client, user):
        data = {
            'username': 'updatedme',
            'password': 'updatedpassword',
            'email': ''
        }
        res = user_client.put('/users/me', data=data)
        assert res.status_code == 200
        assert res.json()['username'] == data['username']
        
    @pytest.mark.django_db
    def test_users_me_delete(self, user_client):
        res = user_client.delete('/users/me')
        assert res.status_code == 204