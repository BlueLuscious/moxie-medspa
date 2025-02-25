from rest_framework import serializers
from api.v1.serializers.medspa_serializer import MedspaSerializer
from medspa.models.medspa_model import MedspaModel
from medspa.models.service_model import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):

    """ Api Serializer for ServiceModel. """

    medspa = MedspaSerializer(read_only=True)
    medspa_id = serializers.PrimaryKeyRelatedField(
        queryset=MedspaModel.objects.all(), write_only=True, source="medspa"
    )

    class Meta:
        model = ServiceModel
        fields = "__all__"
        