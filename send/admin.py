from django.contrib import admin
from .models import Message

from .models import Distribution, Client, Message

admin.site.register(Distribution)
admin.site.register(Client)
admin.site.register(Message)
# Register your models here.
