from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'date', 'status', 'created_at')
    list_filter = ('status', 'service')
    search_fields = ('customer_name', 'service')
