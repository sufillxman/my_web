from django.contrib import admin
from .models import Project, ContactMessage, Certificate, ResumeProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "live_link", "github_link", "created_at")
    search_fields = ("title", "description", "tech_stack")
    list_filter = ("created_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "credential_url", "created_at")
    search_fields = ("title", "issuer")
    list_filter = ("created_at",)