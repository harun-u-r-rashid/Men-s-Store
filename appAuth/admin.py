from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
        list_display=['first_name']

admin.site.register(models.User, UserAdmin)
# Register your models here.
