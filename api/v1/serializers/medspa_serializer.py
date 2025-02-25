from rest_framework import serializers
from medspa.models.medspa_model import MedspaModel


class MedspaSerializer(serializers.ModelSerializer):

    """ Api Serializer for MedspaModel. """

    class Meta:
        model = MedspaModel
        fields = "__all__"
        