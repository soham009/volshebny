from django.contrib import admin
from django.contrib.auth.models import Group
from generateletter.models import Visaletters

# Register your models here.
class VisalettersAdmin(admin.ModelAdmin):
    search_fields = ["Visa_Letter_Number", "Organization", "Payment_status"]
    list_filter = ["Organization", "Payment_status"]
    list_display = [
        "Visa_Letter_Number",
        "Date_of_letter",
        "entry_from",
        "departure_to",
        "Routes_and_Places",
        "no_passenger",
        "Payment_status",
    ]
    list_editable = ["Payment_status"]


admin.site.register(Visaletters, VisalettersAdmin)
admin.site.unregister(Group)
