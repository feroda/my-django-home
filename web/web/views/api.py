from rest_framework import viewsets

from web.models import ArtistQuote, Project
from web.views import serializers


class ArtistQuoteViewSet(viewsets.ModelViewSet):

    lookup_field = 'name'
    lookup_value_regex = '.+'
    queryset = ArtistQuote.objects.all()
    serializer_class = serializers.ArtistQuoteSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    lookup_field = 'name'
    lookup_value_regex = '.+'
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


