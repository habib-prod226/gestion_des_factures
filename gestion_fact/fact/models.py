from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer (models.Model):
    SEX_TYPE=(
        ('M','masculin'),
        ('F','feminin')
    )
    name=models.CharField(max_length=163)
    
    email=models.EmailField( max_length=254)
    
    phone=models.CharField(max_length=125)
    
    adress=models.CharField(max_length=162)
    
    sexe=models.CharField(max_length=1,choices=SEX_TYPE)
    
    age=models.CharField(max_length=15)
    
    city=models.CharField(max_length=32)
    
    zip_code= models.CharField( max_length=16)
    
    created_date= models.DateField(auto_now_add=True)
    
    saved_by=models.ForeignKey(User , on_delete=models.PROTECT)
    
    class Meta:
        verbose_name="Customer"
        verbose_name_plural= "Customers"
        
    def __str__(self):
            return self.name
        
        
class  Invoice (models.Model) :
    """
    Name: Invoice (facture)
    """
    INVOICE_TYPE=(
        ('R','RECUS'),
        ('P','PROFORMA FACTURE'),
        ('F','FACTURE')
    )
    customer= models.ForeignKey(Customer ,on_delete=models.PROTECT)
    
    saved_by=models.ForeignKey(User, on_delete=models.PROTECT)
    
    invoice_date_time =models.DateTimeField(auto_now_add=True)
    
    total =models.DecimalField(max_digits=10000, decimal_places=2)
    
    last_update= models.DateTimeField(null=True, blank=True)
    
    paid= models.BooleanField(default=False)
    
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    
    comments = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name="invoice"
        
        verbose_name_plural ="invoices"
    
    @property
    def get_total_invoice(self):
        articles = self.article_set_all()
        total_invoice= sum(article.get_total for article in articles )

    
    
    
    def __str__(self):
        return f"{self.customer.name}_{self.invoice_date_time}"
    

class Article(models.Model):
    """
    Name: Articles
    Description:
    Author: habibdev226@gmail.com
    """
    invoice= models.ForeignKey(Invoice ,on_delete=models.PROTECT)
    
    name=models.CharField(max_length=32)
    
    quantity=models.IntegerField()
    
    unit_price=models.DecimalField(max_digits=1000,decimal_places=2)
    
    total_articles = models.DecimalField(max_digits=1000,decimal_places=2)
    
    class Meta:
        verbose_name= 'Article'
        verbose_name_plural='Articles'
    
    @property
    def get_total(self):
        total_articles = self.quantity*self.unit_price
        
    def __str__(self):
        return self.name
    