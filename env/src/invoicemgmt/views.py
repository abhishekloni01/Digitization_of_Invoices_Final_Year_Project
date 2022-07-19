# from curses.ascii import HT
from fileinput import filename
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm, CSVFileUploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


#library to import the excel file
import openpyxl
#libraries to create the pdf file and add text to it
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
#library to get logo related information
from PIL import Image


# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab


#csv,pdf libs
from docxtpl import DocxTemplate
import pandas as pd
from win32com import client
import pythoncom
import time
import os

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    # query = list(Invoice.objects.values('line_one'))

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/list_invoice')
    context = {
        "form": form,
        "title": "New Invoice",
        "total_invoices": total_invoices,
		"queryset": queryset,
        # "query":query
    }
    return render(request, "entry.html", context)

@login_required
def list_invoice(request):

    title = 'List of Invoices'
    queryset = Invoice.objects.all()
    

    form = InvoiceSearchForm(request.POST or None)
    csv_upload_form = CSVFileUploadForm()
    context = {"title": title, "queryset": queryset, "form": form, "csv_upload_form":csv_upload_form}

    if request.method == 'POST':
        queryset = Invoice.objects.filter(
            invoice_number__icontains=form['invoice_number'].value(), name__icontains=form['name'].value())
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
            
        }
    if form['generate_invoice'].value() == True:
        instance = queryset
        data_file = instance
        num_of_invoices = len(queryset)
        message = str(num_of_invoices) + " invoices successfully generated."
        messages.success(request, message)

        def import_data(data_file):
            invoice_data = data_file
            for row in invoice_data:
                invoice_type = row.invoice_type
                invoice_number = row.invoice_number
                invoice_date = row.invoice_date
                name = row.name
                phone_number = row.phone_number

                line_one = row.line_one
                line_one_quantity = row.line_one_quantity
                line_one_unit_price = row.line_one_unit_price
                line_one_total_price = row.line_one_total_price

                line_two = row.line_two
                line_two_quantity = row.line_two_quantity
                line_two_unit_price = row.line_two_unit_price
                line_two_total_price = row.line_two_total_price

                line_three = row.line_three
                line_three_quantity = row.line_three_quantity
                line_three_unit_price = row.line_three_unit_price
                line_three_total_price = row.line_three_total_price

                line_four = row.line_four
                line_four_quantity = row.line_four_quantity
                line_four_unit_price = row.line_four_unit_price
                line_four_total_price = row.line_four_total_price

                line_five = row.line_five
                line_five_quantity = row.line_five_quantity
                line_five_unit_price = row.line_five_unit_price
                line_five_total_price = row.line_five_total_price

                line_six = row.line_six
                line_six_quantity = row.line_six_quantity
                line_six_unit_price = row.line_six_unit_price
                line_six_total_price = row.line_six_total_price

                line_seven = row.line_seven
                line_seven_quantity = row.line_seven_quantity
                line_seven_unit_price = row.line_seven_unit_price
                line_seven_total_price = row.line_seven_total_price

                line_eight = row.line_eight
                line_eight_quantity = row.line_eight_quantity
                line_eight_unit_price = row.line_eight_unit_price
                line_eight_total_price = row.line_eight_total_price

                line_nine = row.line_nine
                line_nine_quantity = row.line_nine_quantity
                line_nine_unit_price = row.line_nine_unit_price
                line_nine_total_price = row.line_nine_total_price

                line_ten = row.line_ten
                line_ten_quantity = row.line_ten_quantity
                line_ten_unit_price = row.line_ten_unit_price
                line_ten_total_price = row.line_ten_total_price

                total = row.total
                pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
                generate_invoice(str(name), str(invoice_number), 
                    str(line_one), str(line_one_quantity), str(line_one_unit_price), 
                    str(line_one_total_price), str(line_two), str(line_two_quantity),
                    str(line_two_unit_price), str(line_two_total_price), str(line_three),
                    str(line_three_quantity), str(line_three_unit_price),
                    str(line_three_total_price), str(line_four), str(line_four_quantity),
                    str(line_four_unit_price), str(line_four_total_price),  str(line_five),
                    str(line_five_quantity), str(line_five_unit_price),
                    str(line_five_total_price), str(line_six), str(line_six_quantity),
                    str(line_six_unit_price), str(line_six_total_price), str(line_seven),
                    str(line_seven_quantity), str(line_seven_unit_price),
                    str(line_seven_total_price), str(line_eight), str(line_eight_quantity),
                    str(line_eight_unit_price), str(line_eight_total_price), str(line_nine),
                    str(line_nine_quantity), str(line_nine_unit_price), str(line_nine_total_price), 
                    str(line_ten), str(line_ten_quantity), str(line_ten_unit_price),
                    str(line_ten_total_price), str(total), str(phone_number), str(invoice_date),
                    str(invoice_type), pdf_file_name)

        def generate_invoice(name, invoice_number, 
                line_one, line_one_quantity, line_one_unit_price, line_one_total_price, 
                line_two, line_two_quantity, line_two_unit_price, line_two_total_price, 
                line_three, line_three_quantity, line_three_unit_price, line_three_total_price, 
                line_four, line_four_quantity, line_four_unit_price, line_four_total_price, 
                line_five, line_five_quantity, line_five_unit_price, line_five_total_price, 
                line_six, line_six_quantity, line_six_unit_price, line_six_total_price, 
                line_seven, line_seven_quantity, line_seven_unit_price, line_seven_total_price, 
                line_eight, line_eight_quantity, line_eight_unit_price, line_eight_total_price, 
                line_nine, line_nine_quantity, line_nine_unit_price, line_nine_total_price, 
                line_ten, line_ten_quantity, line_ten_unit_price, line_ten_total_price, 
                total, phone_number, invoice_date, invoice_type, pdf_file_name):
            c = canvas.Canvas(pdf_file_name)

            # image of seal
            logo = 'logo.png'
            c.drawImage(logo, 50, 700, width=500, height=120)

            c.setFont('Helvetica', 12, leading=None)
            # if invoice_type == 'Receipt':
            # 	c.drawCentredString(400, 660, "Receipt Number #:")
            # elif invoice_type == 'Proforma Invoice':
            # 	c.drawCentredString(400, 660, "Proforma Invoice #:")
            # else:
            c.drawCentredString(400, 660, str(invoice_type) + ':')
            c.setFont('Helvetica', 12, leading=None)
            invoice_number_string = str('0000' + invoice_number)
            c.drawCentredString(490, 660, invoice_number_string)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(409, 640, "Date:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(492, 641, invoice_date)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(397, 620, "Amount:")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(484, 622, '$'+total)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(80, 660, "To:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 660, name)

            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(98, 640, "Phone: ")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 640, phone_number)     

            c.setFont('Helvetica-Bold', 14, leading=None)
            c.drawCentredString(310, 580, str(invoice_type))
            c.drawCentredString(110, 560, "Particulars:")
            c.drawCentredString(295, 510, "__________________________________________________________")
            c.drawCentredString(295, 480, "__________________________________________________________")
            c.drawCentredString(295, 450, "__________________________________________________________")
            c.drawCentredString(295, 420, "__________________________________________________________")
            c.drawCentredString(295, 390, "__________________________________________________________")
            c.drawCentredString(295, 360, "__________________________________________________________")
            c.drawCentredString(295, 330, "__________________________________________________________")
            c.drawCentredString(295, 300, "__________________________________________________________")
            c.drawCentredString(295, 270, "__________________________________________________________")
            c.drawCentredString(295, 240, "__________________________________________________________")
            c.drawCentredString(295, 210, "__________________________________________________________")

            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(110, 520, 'ITEMS')     
            c.drawCentredString(220, 520, 'QUANTITY')     
            c.drawCentredString(330, 520, 'UNIT PRICE')     
            c.drawCentredString(450, 520, 'TOTAL')  


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(110, 490, line_one)     
            c.drawCentredString(220, 490, line_one_quantity)     
            c.drawCentredString(330, 490, line_one_unit_price)     
            c.drawCentredString(450, 490, line_one_total_price)     

            if line_two != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 460, line_two)     
                c.drawCentredString(220, 460, line_two_quantity)     
                c.drawCentredString(330, 460, line_two_unit_price)     
                c.drawCentredString(450, 460, line_two_total_price)     

            if line_three != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 430, line_three)     
                c.drawCentredString(220, 430, line_three_quantity)     
                c.drawCentredString(330, 430, line_three_unit_price)     
                c.drawCentredString(450, 430, line_three_total_price)     

            if line_four != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 400, line_four)     
                c.drawCentredString(220, 400, line_four_quantity)     
                c.drawCentredString(330, 400, line_four_unit_price)     
                c.drawCentredString(450, 400, line_four_total_price)     

            if line_five != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 370, line_five)     
                c.drawCentredString(220, 370, line_five_quantity)     
                c.drawCentredString(330, 370, line_five_unit_price)     
                c.drawCentredString(450, 370, line_five_total_price)     

            if line_six != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 340, line_six)     
                c.drawCentredString(220, 340, line_six_quantity)     
                c.drawCentredString(330, 340, line_six_unit_price)     
                c.drawCentredString(450, 340, line_six_total_price)     

            if line_seven != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 310, line_seven)     
                c.drawCentredString(220, 310, line_seven_quantity)     
                c.drawCentredString(330, 310, line_seven_unit_price)     
                c.drawCentredString(450, 310, line_seven_total_price)     

            if line_eight != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 280, line_eight)     
                c.drawCentredString(220, 280, line_eight_quantity)     
                c.drawCentredString(330, 280, line_eight_unit_price)     
                c.drawCentredString(450, 280, line_eight_total_price)     

            if line_nine != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 250, line_nine)     
                c.drawCentredString(220, 250, line_nine_quantity)     
                c.drawCentredString(330, 250, line_nine_unit_price)     
                c.drawCentredString(450, 250, line_nine_total_price)     

            if line_ten != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 220, line_ten)     
                c.drawCentredString(220, 220, line_ten_quantity)     
                c.drawCentredString(330, 220, line_ten_unit_price)     
                c.drawCentredString(450, 220, line_ten_total_price)     



            # TOTAL
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(400, 140, "TOTAL:")
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(484, 140, '$'+total) 


            # SIGN
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(150, 140, "Signed:__________________")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(170, 120, 'Manager') 


            c.showPage()
            # print 'writing'
            c.save()

        import_data(data_file)
    return render(request, "list_invoice.html", context)

@login_required
def list_excel_data(request):
    excelQuerySet = ExcelDataImport.objects.all()
    context = {
        'excelQuerySet': excelQuerySet,
    }
    return render(request,'excelUploadData.html',context)

@login_required
def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_invoice')

    context = {
        'form': form
    }
    return render(request, 'entry.html', context)

@login_required
def update_excel_data(request, pk):
    queryset = ExcelDataImport.objects.get(id=pk)
    print(queryset)
    # if request.method == 'POST':
    #     form = InvoiceUpdateForm(request.POST, instance=queryset)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/list_invoice')

    # context = {
    #     'form': form
    # }
    # return render(request, 'entry.html', context)
    return redirect('list_invoice')


@login_required
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render(request, 'delete_invoice.html')

@login_required
def delete_excel_data(request, pk):
    queryset = ExcelDataImport.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render(request, 'delete_invoice.html')


def create_invoice(sheet):
    to = sheet.cell(row = 2, column =2 ).value
    invoice_type = sheet.cell(row = 2, column = 3).value
    phone = sheet.cell(row = 2, column = 4).value
    date = sheet.cell(row = 2, column = 5).value
    invoice_number = str(1234)


    
    pdf_file_name = str(invoice_type) + '_' + str(to) +'.pdf'
    c = canvas.Canvas(pdf_file_name)

    # image of seal
    logo = 'logo.png'
    c.drawImage(logo, 50, 700, width=200, height=120)

    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(400, 660, str(invoice_type) + ':')
    c.setFont('Helvetica', 12, leading=None)
    invoice_number_string = str('0000' + invoice_number)
    c.drawCentredString(490, 660, invoice_number_string)


    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(409, 640, "Date:")
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(492, 641, date)

    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(98, 640, "Phone: ")
    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(150, 640, str(phone))     

    c.setFont('Helvetica-Bold', 14, leading=None)
    c.drawCentredString(310, 580, str(invoice_type))
    c.drawCentredString(110, 560, "Particulars:")
    c.drawCentredString(295, 510, "__________________________________________________________")
    c.drawCentredString(295, 480, "__________________________________________________________")
    

    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(110, 520, 'ITEMS')     
    c.drawCentredString(220, 520, 'QUANTITY')     
    c.drawCentredString(330, 520, 'UNIT PRICE')     
    c.drawCentredString(450, 520, 'TOTAL')  
    row_count = len(list(sheet.rows))
    print(row_count)
    # column_count = sheet.max_column
    for i in range(2,row_count+1):
        #Reading values from excel file

        item = sheet.cell(row = i, column = 6).value
        quantity = sheet.cell(row = i, column = 7).value
        unit_price = sheet.cell(row = i, column = 8).value
        total = sheet.cell(row = i, column = 9).value
        total_amount = sheet.cell(row = i, column = 10).value
        
        

        c.setFont('Helvetica', 12, leading=None)
        c.drawCentredString(110, 490-(i)*20, item)     
        c.drawCentredString(220, 490-(i)*20, str(quantity))     
        c.drawCentredString(330, 490-(i)*20, str(unit_price))     
        c.drawCentredString(450, 490-(i)*20, str(total))

        

    c.setFont('Helvetica', 12, leading=None)
    c.drawCentredString(397, 620, "Amount:")
    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(484, 622, '$'+str(total_amount))



        
    # TOTAL
    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawCentredString(400, 140, "TOTAL:")
    c.setFont('Helvetica-Bold', 20, leading=None)
    c.drawCentredString(484, 140, '$'+str(total_amount)) 


    # SIGN
    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(150, 140, "Signed:__________________")
    c.setFont('Helvetica-Bold', 12, leading=None)
    c.drawCentredString(170, 120, 'Manager') 


    c.showPage()
    c.save()




def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['choose_file']
        print(uploaded_file.name)

        #convert the font so it is compatible
        pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))

        #import the sheet from the excel file
        wb = openpyxl.load_workbook('C:\\Users\\Abeeshek\\Desktop\\Invoice management system project\\Digitization of Invoice\\env\\src\\InvoiceData.xlsx')
        sheet = wb['invoices2']
        print(len(list(sheet.rows)))

        create_invoice(sheet)
        messages.success(request, 'Successfully Generated Invoice')  
        return redirect('/')

def upload_csv_file(request):
    if request.method=="POST":
        # uploaded_file = request.FILES['document']
        # fs = FileSystemStorage()
        # fs.save(uploaded_file.name,uploaded_file)
        file = CSVFileUploadForm(request.POST, request.FILES)
        if file.is_valid():
            file.save()
    processCSVData()
    return HttpResponse('csv file uploaded!!!')

def processCSVData():
    # word_app = client.Dispatch('Word.Application')
    word_app = client.Dispatch("Word.Application",pythoncom.CoInitialize())
    time.sleep(1)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = ROOT_DIR[:-12]
    file_name = CSVFileUpload.objects.last().csv_file.name
    file_name = file_name.split('/')[1]
    print(file_name)
    file_path = 'C:\\Users\\Abeeshek\\Desktop\\Invoice management system project\\Digitization of Invoice\\env\\src\\media\\csvs'+'\\'+'\\'+file_name

    print(file_path)
    
    data_frame = pd.read_excel(file_path)

    print(data_frame)
    for r_index, row in data_frame.iterrows():
        cust_name = row['Contact_Name']
        print(cust_name)    

        tpl = DocxTemplate(r"C:\Users\Abeeshek\Desktop\Invoice management system project\Digitization of Invoice\env\src\media\csvs\Invoice-Template-doc-margin.docx")
        df_to_doct = data_frame.to_dict()
        x = data_frame.to_dict(orient = 'records')
        context = x
        tpl.render(context[r_index])
        print('before')
        
        
        print(ROOT_DIR)
        tpl.save(ROOT_DIR+'\media\csvs\Docs\\'+cust_name+'.docx')
        print('after')
        time.sleep(2)
        # Get Project Folder Path
        # ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        print(ROOT_DIR)
        #Convert the Docx to PDF file
        doc = word_app.Documents.Open(ROOT_DIR+'\media\csvs\Docs\\' + cust_name + '.docx')
        print('Exporting...')
        doc.SaveAs(ROOT_DIR+'\media\csvs\PDFs\\'+cust_name+'.pdf',FileFormat=17)
        print("Successfully Exported")

    word_app.Quit()
    # messages.success(request,'Successfully Created Invoices')
    return redirect('/')

# def saveExcelDataToDB():