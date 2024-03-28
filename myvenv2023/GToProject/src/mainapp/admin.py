from django.contrib import admin

from mainapp.models import(Frequency,
                           Group,
                           Type,
                           Category,
                           Currency,
                           Unit,
                           Country,
                           Facets,
                           
                            Hits,
                            Info,
                            DataClass,
                             HitsMainClass
                           )


class FrequencyInline(admin.StackedInline):
    model = Frequency
    extra=1
class GroupInline(admin.StackedInline):
    model = Group
    extra=1
class TypeInline(admin.StackedInline):
    model = Type
    extra=1
    
class CategoryInline(admin.StackedInline):
    model = Category
    extra=1
class CurrencyInline(admin.StackedInline):
    model = Currency
    extra=1
    
class UnitInline(admin.StackedInline):
    model = Unit
    extra=1
    
class CountryInline(admin.StackedInline):
    model = Country
    extra=1

class FacetsAdmin(admin.ModelAdmin):
    inlines = [
        FrequencyInline,
          CountryInline,
          UnitInline,
          CurrencyInline,
          CategoryInline,
          TypeInline,
          GroupInline,
             
    ]
    filter_horizontal = ()
    

admin.site.register(Facets,FacetsAdmin)

admin.site.register(HitsMainClass)

  
    

class FacetsInline(admin.StackedInline):
    model = Facets
    extra=1
class CountryAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,    
    ]
    filter_horizontal = ()
    
admin.site.register(Country)
class FrequencyAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Frequency)

class GroupAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Group)

class TypeAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Type)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Category)
class CurrencyAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Currency)
class UnitAdmin(admin.ModelAdmin):
    inlines = [
        FacetsInline,
       
    ]
   
    filter_horizontal = ()
    
admin.site.register(Unit)




class HitssAdmin(admin.ModelAdmin):
  
           
    list_display = ['url','pretty_name',
                    'unit','frequency',
                    'group','type','name',
                    'importance','s',
                    'esID','iids','currency',
                    'category','country','relation','value',
                    
                    
                    ]
    
    
class HitsMainClassInline(admin.StackedInline):
    model = HitsMainClass
    extra=1 
    
class InfoInline(admin.StackedInline):
    model = Info
    extra=1 
    
class   DataClassAdmin(admin.ModelAdmin):
    
    inlines = [
        HitsMainClassInline,
        InfoInline,
       
    ]
   
    filter_horizontal = ()
 
admin.site.register(DataClass,DataClassAdmin)    
    
admin.site.register(Hits)



class HitsInline(admin.StackedInline):
    model = Hits
    extra=1
    
class   InfoAdmin(admin.ModelAdmin):
    
    inlines = [
        HitsInline,
       
    ]
   
    filter_horizontal = ()
 
 
admin.site.register(Info,InfoAdmin)
