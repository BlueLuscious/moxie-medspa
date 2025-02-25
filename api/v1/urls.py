from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.v1.views.appointment_view_set import AppointmentViewSet
from api.v1.views.medspa_view_set import MedspaViewSet
from api.v1.views.service_view_set import ServiceViewSet

router = DefaultRouter()
router.register(r'medspas', MedspaViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
