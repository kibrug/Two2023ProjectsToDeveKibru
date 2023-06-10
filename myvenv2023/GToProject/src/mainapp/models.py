from django.db import models

class TRADINGECONOMICSDATA(models.Model):
    info        = models.CharField(max_length=255)
    santase     = models.IntegerField()
    hits        = models.CharField(max_length=255)
class Info(models.Model):
    info_id    = models.ForeignKey(TRADINGECONOMICSDATA,on_delete=models.CASCADE,related_name='info_id' )
    hits       = models.CharField(max_length=255)
    page       =  models.IntegerField()
    facets     =  models.CharField(max_length=255)
    
class    Hits(models.Model):
    hits_id       = models.ForeignKey(TRADINGECONOMICSDATA,on_delete=models.CASCADE,related_name='hits_id')
    value          = models.IntegerField(default=0)
    relation       = models.CharField(max_length=255)
    country        = models.CharField(max_length=255)
    category       = models.CharField(max_length=255)
    currency       = models.CharField(max_length=255)
    iids           = models.CharField(max_length=255)
    esID           = models.CharField(max_length=255)
    s              = models.CharField(max_length=255)
    importance     = models.IntegerField(default=0)
    name           = models.CharField(max_length=255)
    type           = models.CharField(max_length=255)
    group          = models.CharField(max_length=255)
    frequency      = models.CharField(max_length=255)
    unit           = models.CharField(max_length=255)
    pretty_name    = models.CharField(max_length=255)
    url            = models.CharField(max_length=255)
    

  
class  Hitsrelationvalue(models.Model):
    hits_id       =models.ForeignKey(Info,on_delete=models.CASCADE,related_name='hits_id' )
    value      = models.IntegerField(default=0)
    relation   = models.CharField(max_length=255)
    

class    Facets(models.Model):
    facets_id       =models.ForeignKey(Info,on_delete=models.CASCADE,related_name='facets_id' )
    country         =models.CharField(max_length=255)
    unit            =models.CharField(max_length=255)
    currency        =models.CharField(max_length=255)
    category        =models.CharField(max_length=255)
    type            =models.CharField(max_length=255)
    group           =models.CharField(max_length=255)
    frequency       =models.CharField(max_length=255)
 
   
   

    
class Frequency(models.Model):
    frequency_id      =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='frequency_id' )
    data =             models.DateField(auto_now=False, auto_now_add=False)
    
    key               = models.CharField(max_length=255)
    doc_count         =models.IntegerField(default=0)
    
  

class  Group(models.Model):
    group_id          =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='group_id')
    key               = models.CharField(max_length=255)
    doc_count         =models.IntegerField(default=0)
    
class  Type(models.Model):
    type_id       =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='type_id')
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    

class  Category(models.Model):
    category_id   =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='category_id')
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
class  Currency(models.Model):
    currency_id   =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='currency_id')
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
class   Unit(models.Model):
    unit_id       =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='unit_id')
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    

class    Country(models.Model):
    country_id    =models.ForeignKey( Facets,on_delete=models.CASCADE,related_name='country_id')
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
   

    

    




