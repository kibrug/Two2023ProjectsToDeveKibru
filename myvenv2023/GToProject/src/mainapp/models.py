from django.db import models

class DataClass(models.Model):
    info = models.CharField(max_length=255)
    santase = models.IntegerField()
    hits = models.CharField(max_length=255)
class    Info(models.Model):
   
    hits_name     = models.ForeignKey(DataClass,on_delete=models.CASCADE,related_name='hits_name' )
    page      =  models.IntegerField()
    facets    =  models.CharField(max_length=255)
#, related_name='hits'    
class    Hits(models.Model):
    hits       =models.ForeignKey(Info,on_delete=models.CASCADE)
    value      = models.IntegerField(default=0)
    relation   = models.CharField(max_length=255)
    

class    Facets(models.Model):
    
    country_name    =models.CharField(max_length=255)
    unit_name       =models.CharField(max_length=255)
    currency_name   =models.CharField(max_length=255)
    category_name   =models.CharField(max_length=255)
    type_name       =models.CharField(max_length=255)
    group_name      =models.CharField(max_length=255)
    frequency_name  =models.CharField(max_length=255)
 
   
   

    
class Frequency(models.Model):
    frequency  =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
  

class  Group(models.Model):
    group      =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
class  Type(models.Model):
    type       =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    

class  Category(models.Model):
    category   =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
class  Currency(models.Model):
    currency   =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    
class   Unit(models.Model):
    unit       =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
    

class    Country(models.Model):
    country    =models.ForeignKey( Facets,on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    doc_count =models.IntegerField(default=0)
   

    
class    HitsMainClass(models.Model):
    dataclas = models.ForeignKey(DataClass,on_delete=models.CASCADE)
    value      = models.IntegerField(default=0)
    relation   = models.CharField(max_length=255)
    country     = models.CharField(max_length=255)
    category     = models.CharField(max_length=255)
    currency     = models.CharField(max_length=255)
    iids         = models.CharField(max_length=255)
    esID        = models.CharField(max_length=255)
    s           = models.CharField(max_length=255)
    importance   = models.IntegerField(default=0)
    name         = models.CharField(max_length=255)
    type         = models.CharField(max_length=255)
    group        = models.CharField(max_length=255)
    frequency    = models.CharField(max_length=255)
    unit         = models.CharField(max_length=255)
    pretty_name   = models.CharField(max_length=255)
    url            = models.CharField(max_length=255)
    




