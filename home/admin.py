from django.contrib import admin
from . models import messages
from . models import contact
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import VIDEO
from .models import TodoItem

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(TodoItem)
admin.site.register(VIDEO, MyModelAdmin)
admin.site.register(messages)
admin.site.register(contact)
