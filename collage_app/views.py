from django.http.response import Http404, HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND
import time


from .serializers import TokenSerializer, SerieSerializer
from .models import Token, Serie

class TokenList(APIView):
    def get(self, request, format=None):
        token = Token.objects.filter(serie__choices="SOLD").order_by('?')
        time.sleep(10)
        serializer =  TokenSerializer(token, many=True)
        return Response(serializer.data)


class SeriedToken(ModelViewSet):
    queryset = Serie.objects.filter(choices='SOLD')
    serializer_class = SerieSerializer

    def get_queryset(self):
        return self.queryset

    def get_object(self):
        serie_slug = self.kwargs['pk']
        return self.get_queryset().get(slug=serie_slug)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except (Serie.DoesNotExist, KeyError):
            return Response({"error": "Requested Movie does not exist"}, status=HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset    = self.get_queryset()
        serializer  = self.get_serializer(queryset, many=True)
        return Response(serializer.data)