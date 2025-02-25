from rest_framework import viewsets
from medspa.models.medspa_model import MedspaModel
from api.v1.serializers.medspa_serializer import MedspaSerializer


class MedspaViewSet(viewsets.ModelViewSet):

    """ ViewSet for MedspaModel. """

    queryset = MedspaModel.objects.all()
    serializer_class = MedspaSerializer
    