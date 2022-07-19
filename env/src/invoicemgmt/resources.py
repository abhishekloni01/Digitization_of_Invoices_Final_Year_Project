from import_export import resources
from invoicemgmt.models import ExcelDataImport

class ExcelDataImportResource(resources.ModelResource):
    class Meta:
        model = ExcelDataImport
        fields = ('id','to','invoice_type','phone','date','item','quantity','unit_price','total','amount')