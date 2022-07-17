#library to import the excel file
import openpyxl
#libraries to create the pdf file and add text to it
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
#library to get logo related information
from PIL import Image

#convert the font so it is compatible
pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))

#import the sheet from the excel file
wb = openpyxl.load_workbook('C:\\Users\\Abeeshek\\Desktop\\Invoice management system project\\Digitization of Invoice\\env\\src\\InvoiceData.xlsx')
sheet = wb['invoices']

#import company's logo
im = Image.open('C:\\Users\\Abeeshek\\Desktop\\Invoice management system project\\Digitization of Invoice\\env\\src\\logo.png   ')
width, height = im.size
ratio = width/height
image_width = 400
image_height = int(image_width / ratio)

#Page information
page_width = 2156
page_height = 3050

#Invoice variables
company_name ='The best company in the world'
payment_terms = 'x'
contact_info = 'x'
margin = 100
month_year = 'August 2019'

#def function
def create_invoice():
    for i in range(2,3):
        #Reading values from excel file
        to = sheet.cell(row = i, column =1 ).value
        invoice_type = sheet.cell(row = i, column = 2).value
        phone = sheet.cell(row = i, column = 3).value
        date = sheet.cell(row = i, column = 4).value
        item = sheet.cell(row = i, column = 5).value.lower()
        quantity = sheet.cell(row = i, column = 6).value
        unit_price = sheet.cell(row = i, column = 7).value
        total = sheet.cell(row = i, column = 8).value
        total_amount = sheet.cell(row = i, column = 9).value

        #Creating a pdf file and setting a naming convention
        c = canvas.Canvas(str(invoice_type) + '_' + str(to) +'.pdf')
        c.setPageSize((page_width, page_height))

        #Drawing the image
        c.drawInlineImage("C:\\Users\\Abeeshek\\Desktop\\Invoice management system project\\Digitization of Invoice\\env\\src\\logo.png", page_width - image_width - margin,
                          page_height - image_height - margin,
                          image_width, image_height)

        #Invoice information
        c.setFont('Arial',80)
        text = 'INVOICE'
        text_width = stringWidth(text,'Arial',80)
        c.drawString((page_width-text_width)/2, page_height - image_height - margin, text)
        y = page_height - image_height - margin*4
        x = 2*margin
        x2 = x + 550
        
        c.setFont('Arial', 45)
        c.drawString(x, y, 'Issued by: ')
        c.drawString(x2,y, company_name)
        y -= margin
        
        c.drawString(x,y,'Issued to: ')
        c.drawString(x2,y,to)
        y -= margin
        
        c.drawString(x,y,'Invoice type: ')
        c.drawString(x2,y, str(invoice_type))
        y -= margin
        
        c.drawString(x,y, 'Phone: ')
        c.drawString(x2,y, phone)
        y -= margin
        
        c.drawString(x,y,'Due date: ')
        c.drawString(x2,y, date)
        y -= margin *2
        
        c.drawString(x,y,'Invoice issued for performed '+ item + ' for ' + month_year)
        y -= margin *2
        
        c.drawString(x,y, 'Amount excluding unit_price: ')
        c.drawString(x2,y, 'EUR ' + str(quantity))
        y -= margin
        
        c.drawString(x,y,'Value added tax: ')
        c.drawString(x2,y, 'EUR ' + str(unit_price))
        y-= margin
        
        c.drawString(x,y,'Total amount: ')
        c.drawString(x2,y,'EUR ' + str(total_amount))
        y -= margin*3
               
        c.drawString(x,y,'If paid within 10 days, 2% of discount is granted.')
        y -= margin
        c.drawString(x,y,'Bank account number: 1234 ABCD 4567 EFGH')
        y -= margin
        c.drawString(x,y,'In case of any questions, contact info@thebestcompany.com')    

        #Saving the pdf file
        c.save()

create_invoice()