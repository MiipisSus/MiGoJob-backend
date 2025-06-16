import factory
from pytest_factoryboy import register
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User


DEFAULT_PASSWORD = 'defaultpassword123'

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    
    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password(DEFAULT_PASSWORD)
        
        self.save()
        
        
register(UserFactory)