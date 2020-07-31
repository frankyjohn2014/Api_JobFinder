from rest_framework.viewsets import ModelViewSet
from scraping.models import City, Language, Vacancy
from .serializers import *

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
# class VacancyViewSet(ModelViewSet):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancySerializer



