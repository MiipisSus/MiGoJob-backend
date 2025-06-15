from ninja.errors import HttpError
from ninja_jwt.authentication import JWTAuth

class IsAuthenticated(JWTAuth):
    pass

class IsSuperuser(JWTAuth):
    def authenticate(self, request, key):
        user = super().authenticate(request, key)
        if user and user.is_superuser:
            return user
        else:
            raise HttpError(403, 'Forbidden')