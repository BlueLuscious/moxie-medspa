from decimal import Decimal
from django.db import models
from django.db.models import QuerySet
from medspa.models.medspa_model import MedspaModel
from medspa.models.choices.appointment_status_choices import AppointmentStatusChoices
from medspa.models.service_model import ServiceModel


class AppointmentModel(models.Model):

    """
    Appointment Model.

    Fields:
        id (int): Unique identifier.
        start_time (datetime): Appointment beginning.
        status (str): Appointment status.
        medspa (MedspaModel): Medspa instance.
        services (QuerySet[ServiceModel]): Service instances.
    """

    id = models.BigAutoField(primary_key=True, unique=True)
    start_time = models.DateTimeField()
    status = models.CharField(
        max_length=24,
        choices=AppointmentStatusChoices.choices,
        default=AppointmentStatusChoices.SCHEDULED
    )
    medspa = models.ForeignKey(
        MedspaModel, models.DO_NOTHING, related_name="appointments"
    )
    services: QuerySet[ServiceModel] = models.ManyToManyField(
        ServiceModel, related_name="appointments"
    )


    def __str__(self) -> str:
        return f"Appointment: {self.id}"
    
    @property
    def total_duration(self) -> int:
        if self.services.exists():
            return sum(service.duration for service in self.services.all())
        else:
            return 0

    @property
    def total_price(self) -> Decimal:
        if self.services.exists():
            return sum(service.price for service in self.services.all())
        else:
            return 0
    