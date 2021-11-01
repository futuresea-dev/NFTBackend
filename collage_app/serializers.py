from rest_framework import serializers
from .models import Serie, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            'collection_id',
            'description',
            'title',
            'image',
            'status',
            'token_id'
        ]


class SerieSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True, read_only=True)

    class Meta:
        model = Serie
        fields = [
            'collection_id',
            'description',
            'title',
            'image',
            'status',
            'token_id'
        ]
