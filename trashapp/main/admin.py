from django.contrib import admin
from .models import DistanceMeasurement

# Register your models here.
@admin.register(DistanceMeasurement)
class DistanceMeasurementAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)