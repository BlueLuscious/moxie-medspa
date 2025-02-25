from django.contrib import admin
from medspa.models.appointment_model import AppointmentModel


@admin.register(AppointmentModel)
class AppointmentAdmin(admin.ModelAdmin):

    """ Admin for AppointmentModel. """

    list_display = (
        "id",
        "start_time",
        "total_duration",
        "total_price",
        "status",
        "medspa",
        "get_services",
    )
       
    def get_services(self, obj: AppointmentModel) -> str:
        return ", ".join(
            [service.__str__() for service in obj.services.all()]
        ) if obj.services.exists() else "N/A"
    get_services.short_description = "Services ID"
    