from django.contrib import admin
from .views import Invoice, InvoiceDetail

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
