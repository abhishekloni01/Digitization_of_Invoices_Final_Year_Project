from import_export import resources
from invoicemgmt.models import ExcelDataImport

class ExcelDataImportResource(resources.ModelResource):
    class Meta:
        model = ExcelDataImport
    fields = ('id','Contact_Name','Company_Name','Phone','Date','Invoice_Number','Email','Item','Quantity','Unit_Price','Total','Discount','Balance_Due')