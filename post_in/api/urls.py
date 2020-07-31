from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls

# note_list = NoteViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })
# note_detail = NoteViewSet.as_view({
#     'get':'retrieve',
#     'put':'update',
#     'patch':'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = [
#     # path('notes/',notes_list),
#     # path('notes/<int:pk>/',notes_detail),
#     # path('notes/',NoteListView.as_view()),
#     # path('notes/<int:pk>/',NoteDetailView.as_view(), name='note_detail'),
#     path('notes/',note_list, name='note_list'),
#     path('notes/<int:pk>/',note_detail, name='note_detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)