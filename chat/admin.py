from django.contrib import admin

from chat.models import Message
from chat.models import Chat

class Messageadmin(admin.ModelAdmin):
    fields = ('chat','text','created_at','author', 'receiver')
    list_display = ('created_at', 'author', 'text', 'receiver')
    search_fields = ('text',)
    

# Register your models here.

admin.site.register(Message, Messageadmin)
admin.site.register(Chat)