from django.contrib.auth.models import User
from ninja import ModelSchema


class UserIn(ModelSchema):
    class Meta:
        model = User
        fields = ["username", "password", "email"]

class UserOut(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "email"]