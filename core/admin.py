from django.contrib import admin

# Register your models here.
from .models import Project, Skill, Message

admin.site.register(Project)
admin.site.register(Skill)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')


admin.site.register(Message, MessageAdmin)