from rest_framework import viewsets
from . import models
from rest_framework.response import Response
from . serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class Persons(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    # def list(self, request):
    #     queryset = models.Person.objects.all()
    #     ser = PersonSerializer(queryset, many=True)
    #     return Response(ser.data, status=status.HTTP_200_OK)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = get_object_or_404(models.Person, pk=pk)
    #     ser = PersonSerializer(queryset)
    #     return Response(ser.data, status=status.HTTP_200_OK)
    #
    # def create(self, request):
    #     ser = PersonSerializer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
