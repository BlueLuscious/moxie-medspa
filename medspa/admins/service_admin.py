from django.contrib import admin
from medspa.models.service_model import ServiceModel


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):

    """ Admin for ServiceModel. """

    list_display = (
        "id",
        "name",
        "price",
        "duration",
        "medspa",
        "get_appointments",
    )
    
    def get_appointments(self, obj: ServiceModel) -> str:
        return ", ".join(
            [appointment.__str__() for appointment in obj.appointments.all()]
        ) if obj.appointments.exists() else "N/A"
    get_appointments.short_description = "Appointments ID"
    