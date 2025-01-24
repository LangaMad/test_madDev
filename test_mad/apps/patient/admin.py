from django.contrib import admin
from .models import Patient
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin,DynamicArrayMixin):

    list_display = ['id', 'first_name', 'last_name', 'created_at']
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

