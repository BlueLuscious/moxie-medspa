from typing import TYPE_CHECKING
from django.db import models
from django.db.models import QuerySet
if TYPE_CHECKING:
    from medspa.models.appointment_model import AppointmentModel
    from medspa.models.service_model import ServiceModel


class MedspaModel(models.Model):

    """
    Service Model.

    Fields:
        id (int): Unique identifier.
        name (str): Consumer name.
        address (str): Consumer address.
        phone_number (str): Consumer phone number.
        email_address (str): Consumer email address.

    Related Fields:
        appointments (QuerySet[AppointmentModel]): Appointment instances.
        services (QuerySet[ServiceModel]): Service instances.
    """

    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    email_address = models.EmailField(max_length=256, unique=True)

    appointments: "QuerySet[AppointmentModel]"
    services: "QuerySet[ServiceModel]"


    def __str__(self) -> str:
        return f"Mesdpa: {self.name} - {self.id}"
    