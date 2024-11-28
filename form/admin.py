from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')  # Fields to display in the list view

admin.site.register(Contact, ContactAdmin)

