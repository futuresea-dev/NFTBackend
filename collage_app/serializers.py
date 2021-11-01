from rest_framework import serializers
from .models import Serie, Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            'number',
            'author',
            'get_image',
            'serie',
            'title',
        ]

class SerieSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True, read_only=True)
    class Meta:
        model = Serie
        fields = [
            'title',
            'get_image',
            'description',
            'get_absolute_url',
            'slug',
            'tokens',
            'choices'
        ]