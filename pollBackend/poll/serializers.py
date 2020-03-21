from rest_framework import serializers
from .models import Pollingoption, Pollingtitle


class PolloptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'option',
            'vote',
        )
        model = Pollingoption


class PolltitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'title',
        )
        model = Pollingtitle
