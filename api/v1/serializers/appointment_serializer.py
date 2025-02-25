from rest_framework import serializers
from api.v1.serializers.medspa_serializer import MedspaSerializer
from api.v1.serializers.service_serializer import ServiceSerializer
from medspa.models.appointment_model import AppointmentModel
from medspa.models.medspa_model import MedspaModel
from medspa.models.service_model import ServiceModel


class AppointmentSerializer(serializers.ModelSerializer):

    """ Api Serializer for AppointmentModel. """

    medspa = MedspaSerializer(read_only=True)
    medspa_id = serializers.PrimaryKeyRelatedField(
        queryset=MedspaModel.objects.all(), write_only=True, source="medspa"
    )
    services = ServiceSerializer(many=True, read_only=True)
    services_ids = serializers.PrimaryKeyRelatedField(
        queryset=ServiceModel.objects.all(), write_only=True, source="services", many=True
    )
    total_duration = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentModel
        fields = "__all__"

    def get_total_duration(self, obj: AppointmentModel) -> int:
        return obj.total_duration

    def get_total_price(self, obj: AppointmentModel) -> float:
        return float(obj.total_price)
    