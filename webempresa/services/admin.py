from django.contrib import admin
from .models import Service
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Service,ServicesAdmin)