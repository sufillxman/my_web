from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ContactMessageViewSet, CertificateViewSet, ResumeViewSet

router = DefaultRouter()

router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"contact", ContactMessageViewSet, basename="contact")
router.register(r"certificates", CertificateViewSet, basename="certificates")
router.register(r"resume", ResumeViewSet, basename="resume")

urlpatterns = [
    path("", include(router.urls)),
]
