from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Project, ContactMessage, Certificate, ResumeProfile
from .serializers import (
    ProjectSerializer,
    ContactMessageSerializer,
    CertificateSerializer,
    ResumeSerializer,
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public API endpoint for portfolio projects.
    Supports:
    GET /api/projects/
    GET /api/projects/{id}/
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public API endpoint for certificates.
    Supports:
    GET /api/certificates/
    GET /api/certificates/{id}/
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [AllowAny]


class ContactMessageViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    Public API endpoint for contact form submissions.
    Supports:
    POST /api/contact/
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Email notifications are disabled until SMTP is configured.
        # The contact data is still saved to the backend for review.
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public API endpoint for resume content.
    Supports:
    GET /api/resume/
    """
    queryset = ResumeProfile.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        resume_data = {
            "name": "Sufill X Man (Manknojiya Sufiyan)",
            "role": "AI + Web + API Fullstack Developer (Target: 2026)",
            "phone": "7405721856",
            "email": "sufillxman@gmail.com",
            "linkedin": "https://linkedin.com/in/sufill-x-man/",
            "github": "https://github.com/sufillxman",
            "instagram": "https://instagram.com/sufilldigital/",
            "summary": "BCA student building automation-first fullstack experiences with Django, DRF, React, and polished UIs.",
            "skills": [
                "HTML", "CSS", "JavaScript",
                "Bootstrap", "CSS Grid", "Flexbox",
                "React.js", "Redux Toolkit", "Tailwind CSS",
                "Python", "Django", "Django REST Framework",
                "MySQL", "C Programming",
                "Problem-Solving & Debugging",
                "Video Editing", "Graphic Design", "Digital Marketing"
            ],
            "education": [
                "Bachelor of Computer Applications (BCA) - In Progress",
                "Web Development Course - Xipra Technology (Completed)"
            ],
            "highlights": [
                "Custom billing and inventory automation for retail mobile businesses.",
                "Instagram clone with secure admin management built in Python.",
                "Modern UI design work for hotels, shops, and companies using Tailwind and Bootstrap.",
                "Database-driven resume and headless CMS architecture for faster editing."
            ],
        }
        resume, created = ResumeProfile.objects.get_or_create(defaults={**resume_data})
        if not created:
            # Make sure defaults exist in DB if model exists but some fields are missing
            updated = False
            for field, value in resume_data.items():
                if getattr(resume, field) in (None, '', []):
                    setattr(resume, field, value)
                    updated = True
            if updated:
                resume.save()

        serializer = self.get_serializer(resume)
        return Response([serializer.data])
