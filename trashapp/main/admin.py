from django.contrib import admin
from .models import DistanceMeasurement, TrashCan

# Register your models here.
@admin.register(DistanceMeasurement)
class DistanceMeasurementAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

@admin.register(TrashCan)
class TrashCanAdmin(admin.ModelAdmin):
    pass