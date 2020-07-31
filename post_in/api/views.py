from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.models import Note
from api.serializers import NoteSerializer,ThisNoteSerializer,UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin 
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from accounts.models import User
class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.object.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


#all in one
class NoteViewSet(ModelViewSet):
    # queryset = Note.objects.all()
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    # http_method_names = ['get','post']

    def list(self, request, *args, **kwargs):

        notes = Note.objects.all()
        # notes = Note.objects.filter(author=request.user.id)
        context = {'request': request}
        serializer = ThisNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
# #generic view get post
# class NoteListView(ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def list(self, request, *args, **kwargs):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThisNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)
# #generic view put update delete
# class NoteDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# #Вью на миксинах
# class NoteListView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = ThisNoteSerializer
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# #detailmixinview
# class NoteDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,GenericAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#Вьюха на классах
# class NoteListView(APIView):
#     def get(self, request, format=None):
#         notes = Note.objects.all()
#         context = {'request':request}
#         serializer = ThisNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Вьюха на классах детальная
# class NoteDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except note.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)

#     def put(self, request,pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,pk, format=None):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def notes_list(request, format=None):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def notes_detail(request, pk,format=None):
#     try:
#         note = Note.objects.get(pk=pk)
#     except note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
