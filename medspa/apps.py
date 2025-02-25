from django.apps import AppConfig


class MedspaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "medspa"


    def ready(self) -> None:
        
        from .models import  (
            appointment_model,
            medspa_model,
            service_model,
        )
        
        from .admins import  (
            appointment_admin,
            medspa_admin,
            service_admin,
        )
