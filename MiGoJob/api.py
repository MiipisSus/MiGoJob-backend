from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from apps.companies.api import router as companies_router
from apps.jobs.api import router as jobs_router
from apps.users.api import router as users_router

api = NinjaExtraAPI()

api.add_router('companies', companies_router)
api.add_router('jobs', jobs_router)
api.add_router('users', users_router)

api.register_controllers(NinjaJWTDefaultController)