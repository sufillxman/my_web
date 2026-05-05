from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=300,
        help_text="Comma-separated technologies, e.g. React, Django, MySQL"
    )
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ResumeProfile(models.Model):
    name = models.CharField(max_length=200, default="Sufill X Man (Manknojiya Sufiyan)")
    role = models.CharField(max_length=200, default="AI + Web + API Fullstack Developer")
    phone = models.CharField(max_length=50, blank=True, default="7405721856")
    email = models.EmailField(blank=True, default="sufillxman@gmail.com")
    linkedin = models.URLField(blank=True, default="https://linkedin.com/in/sufill-x-man/")
    github = models.URLField(blank=True, default="https://github.com/sufillxman")
    instagram = models.URLField(blank=True, default="https://instagram.com/sufilldigital/")
    summary = models.TextField(default="BCA student and fullstack builder creating automation-first web systems with Django, React and REST APIs.")
    skills = models.JSONField(default=list)
    education = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Resume Profile"
        verbose_name_plural = "Resume Profiles"

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    credential_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title