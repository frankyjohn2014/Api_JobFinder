import datetime
from rest_framework.viewsets import ModelViewSet
from scraping.models import City, Language, Vacancy
from .serializers import *

period = datetime.date.today()-datetime.timedelta(1)

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
class VacancyViewSet(ModelViewSet):
    """?city=minsk&language=python """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_queryset(self):
        city_slug = self.request.query_params.get('city', None)
        language_slug = self.request.query_params.get('language', None)
        qs = None
        if city_slug and language_slug:
            qs = Vacancy.objects.filter(city__slug=city_slug, language__slug=language_slug, timestamp__gte=period)
        self.queryset = qs
        return self.queryset




