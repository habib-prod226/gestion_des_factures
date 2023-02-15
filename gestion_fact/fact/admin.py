from django.contrib import admin
from .models import *
 
# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display=('name', 'email', 'adress', 'phone', 'sexe', 'age',  'city', 'zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer','saved_by', 'invoice_date_time', 'total','invoice_type','paid')
    
admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)  
