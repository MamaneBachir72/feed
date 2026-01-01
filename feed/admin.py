from django.contrib import admin
from feed.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']


# Register your models here.
admin.site.register(Message, MessageAdmin)