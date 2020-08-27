from rest_framework import routers
from home.api_views import Persons

router = routers.DefaultRouter()
router.register('', Persons, basename='person')