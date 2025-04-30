from rest_framework import serializers
from web.models import ArtistQuote, Project


class ArtistQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistQuote
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

