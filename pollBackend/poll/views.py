from rest_framework import generics
from .models import Pollingoption,Pollingtitle
from rest_framework import viewsets
from .serializers import PolloptionSerializer, PolltitleSerializer
from rest_framework.response import Response
from django.http import Http404


# class Polloptiondata(generics.ListCreateAPIView):
#     queryset1 = Pollingoption.objects.all()
#     serializer_class = PolloptionSerializer


# class Polltitledata(generics.ListCreateAPIView):
#     queryset2 = Pollingtitle.objects.all()
#     serializer_class = PolltitleSerializer

class Polloptiondata(generics.ListCreateAPIView):
    queryset = Pollingoption.objects.all()
    serializer_class = PolloptionSerializer

    def perform_destroy(self, instance): 
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class Polltitledata(generics.ListCreateAPIView):
    queryset = Pollingtitle.objects.all()
    serializer_class = PolltitleSerializer

    def perform_destroy(self, instance): 
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

