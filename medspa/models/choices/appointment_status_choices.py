from django.db import models


class AppointmentStatusChoices(models.TextChoices):

    """ Status Choices for AppointmentModel. """

    SCHEDULED = "SCHEDULED", "scheduled"
    COMPLETED = "COMPLETED", "completed"
    CANCELED = "CANCELED", "canceled"
