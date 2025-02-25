from rest_framework import viewsets
from medspa.models.appointment_model import AppointmentModel
from api.v1.serializers.appointment_serializer import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):

    """ ViewSet for AppointmentModel. """

    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
