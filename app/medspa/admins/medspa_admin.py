from django.contrib import admin
from medspa.models.medspa_model import MedspaModel


@admin.register(MedspaModel)
class MedspaAdmin(admin.ModelAdmin):

    """ Admin for MedspaModel. """

    list_display = (
        "id",
        "name",
        "address",
        "phone_number",
        "email_address",
        "get_appointments",
        "get_services",
    )

    def get_appointments(self, obj: MedspaModel) -> str:
        return ", ".join(
            [appointment.__str__() for appointment in obj.appointments.all()]
        ) if obj.appointments.exists() else "N/A"
    get_appointments.short_description = "Appointments ID"
        
    def get_services(self, obj: MedspaModel) -> str:
        return ", ".join(
            [service.__str__() for service in obj.services.all()]
        ) if obj.services.exists() else "N/A"
    get_services.short_description = "Services ID"
    