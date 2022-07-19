from binascii import Incomplete
from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm

from import_export.admin import ImportExportModelAdmin
from .models import ExcelDataImport
from .resources import ExcelDataImportResource


class ExcelImportAdmin(ImportExportModelAdmin):
   resource_class = ExcelDataImportResource
   # list_display = ("to", "invoice_type", "phone", "date", "item", "quantity", "unit_price", "total" ,"amount")
   


class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['name', 'invoice_number', 'invoice_date']
   form = InvoiceForm
#    list_filter = ['name']
#    search_fields = ['name', 'invoice_number']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(ExcelDataImport, ExcelImportAdmin)
