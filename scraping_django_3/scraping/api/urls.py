from rest_framework import routers
from .views import *

routers = routers.DefaultRouter()
routers.register('cities',CityViewSet)
routers.register('sp',LanguageViewSet)
routers.register('vacancy',VacancyViewSet)
urlpatterns = routers.urls

