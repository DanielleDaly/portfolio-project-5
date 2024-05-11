from django.contrib import admin
from .models import CustomerEnquiry


class CustomerEnquiryAdmin(admin.ModelAdmin):
    readonly_fields = ('enquiry_number', 'date',)

    fields = ('enquiry_number', 'date', 'full_name',
              'email', 'phone_number', 'enquiry', 'country',)

    list_display = ('enquiry_number', 'date', 'full_name',
                    'email', 'phone_number',)

    ordering = ('-date',)


admin.site.register(CustomerEnquiry, CustomerEnquiryAdmin)
