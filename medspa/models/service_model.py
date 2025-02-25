from typing import TYPE_CHECKING
from django.db import models
from django.db.models import QuerySet
from medspa.models.medspa_model import MedspaModel
if TYPE_CHECKING:
    from medspa.models.appointment_model import AppointmentModel
    


class ServiceModel(models.Model):

    """
    Service Model.

    Fields:
        id (int): Unique identifier.
        name (str): Service name.
        description (str): Service description.
        price (Decimal): Service price.
        duration (int): Service duration.
        medspa (MedspaModel): Medspa instance.

    Related Fields:
        appointments (QuerySet[AppointmentModel]): Appointment instances.
    """

    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    medspa = models.ForeignKey(
        MedspaModel, models.DO_NOTHING, related_name="services"
    )

    appointments: "QuerySet[AppointmentModel]"


    def __str__(self) -> str:
        return f"Service: {self.name} - {self.id}"
    