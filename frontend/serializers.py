from rest_framework import serializers
from .models import Character, Quote


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['url', 'name']


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = ['url', 'quote_text', 'character']