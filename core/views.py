import requests
from django.conf import settings
from rest_framework import generics
from .models import Project, Skill, Message
from .serializers import ProjectSerializer, SkillSerializer, MessageSerializer


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillListView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        msg = serializer.save()
        try:
            requests.post(
                "https://api.brevo.com/v3/smtp/email",
                headers={"api-key": settings.BREVO_API_KEY},
                json={
                    "sender": {"name": "Portfolio", "email": settings.BREVO_SENDER_EMAIL},
                    "to": [{"email": settings.CONTACT_RECEIVER_EMAIL}],
                    "replyTo": {"email": msg.email},
                    "subject": f"[Portfolio] {msg.subject}",
                    "textContent": f"De : {msg.name} ({msg.email})\n\n{msg.message}",
                },
                timeout=10,
            )
        except Exception:
            pass