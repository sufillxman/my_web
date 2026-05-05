from rest_framework import serializers
from .models import Project, ContactMessage, Certificate, ResumeProfile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tech_stack",
            "image",
            "live_link",
            "github_link",
            "created_at",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "message",
            "created_at",
        ]
        read_only_fields = ["created_at"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "title",
            "issuer",
            "credential_url",
            "created_at",
        ]


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeProfile
        fields = [
            "id",
            "name",
            "role",
            "phone",
            "email",
            "linkedin",
            "github",
            "instagram",
            "summary",
            "skills",
            "education",
            "highlights",
            "updated_at",
        ]
