from django.urls import path
from .views import ProjectListView, SkillListView, MessageCreateView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('skills/', SkillListView.as_view()),
    path('contact/', MessageCreateView.as_view()),
]