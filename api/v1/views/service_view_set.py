from rest_framework import viewsets
from medspa.models.service_model import ServiceModel
from api.v1.serializers.service_serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):

    """ ViewSet for ServiceModel. """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
