from django.contrib import admin

from core.models import Transport, Reservation, Performer, Customer


class ReservationAdmin(admin.ModelAdmin):
    search_fields = ('transport__name', 'transport__type', )


class TransportAdmin(admin.ModelAdmin):
    search_fields = ('name', 'type', )
    list_filter = ('type', )


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Performer)
admin.site.register(Customer)
