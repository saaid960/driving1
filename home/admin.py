from django.contrib import admin
from . models import messages
from . models import contact
admin.site.register(messages)
admin.site.register(contact)
