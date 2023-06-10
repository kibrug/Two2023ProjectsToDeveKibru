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
                            TRADINGECONOMICSDATA,
                              Hitsrelationvalue
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
    
    list_display = ['facets_id',
                    'country',
                    'unit',
                    'type',
                    'group',
                    'frequency',
                    'currency',
                    'category',
                    
                    
                    ]
    
    
    filter_horizontal = ()
    

admin.site.register(Facets,FacetsAdmin)




class CountryAdmin(admin.ModelAdmin):
     
    list_display = ['country_id',
                    'key',
                    'doc_count',
   
                    ]
 
    filter_horizontal = ()
    
admin.site.register(Country,CountryAdmin)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ['frequency_id',
                    'key',
                    'doc_count',
   
                    ]
   
    filter_horizontal = ()
    
admin.site.register(Frequency,FrequencyAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_id',
                    'key',
                    'doc_count',
   
                    ]
   
   
    filter_horizontal = ()
    
admin.site.register(Group,GroupAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ['type_id',
                    'key',
                    'doc_count',
   
                    ]
   
    filter_horizontal = ()
    
admin.site.register(Type,TypeAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id',
                    'key',
                    'doc_count',
   
                    ]
   
    filter_horizontal = ()
    
admin.site.register(Category,CategoryAdmin)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['currency_id',
                    'key',
                    'doc_count',
   
                    ]
   
   
    filter_horizontal = ()
    
admin.site.register(Currency)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit_id',
                    'key',
                    'doc_count',
   
                    ]
   
   
    filter_horizontal = ()
    
admin.site.register(Unit,UnitAdmin)




class HitssAdmin(admin.ModelAdmin):
  
           
    list_display = ['url',
                    'pretty_name',
                    'unit',
                    'frequency',
                    'group',
                    'type',
                    'name',
                    'importance',
                    's',
                    'esID',
                    'iids',
                    'currency',
                    'category',
                    'country',
                    'relation',
                    'value',
                    
                    
                    ]
admin.site.register(Hits,HitssAdmin)

class HitsrelationvalueAdmin(admin.ModelAdmin):
     
    list_display = ['hits_id',
                    'value',
                    'relation',
                   
                    ]
    
admin.site.register(Hitsrelationvalue,HitsrelationvalueAdmin)
    
    
class HitsInline(admin.StackedInline):
    model = Hits
    extra=1 
    
class InfoInline(admin.StackedInline):
    model = Info
    extra=1 
    
class   TRADINGECONOMICSDATAdmin(admin.ModelAdmin):
    
    
    inlines = [
        HitsInline,
        InfoInline,
       
    ]
   
    list_display = ['info',
                    'santase',
                    'hits',
                   
                    ]
   
    filter_horizontal = ()
 
admin.site.register(TRADINGECONOMICSDATA,TRADINGECONOMICSDATAdmin)    
    




class HitsrelationvalueInline(admin.StackedInline):
    model = Hitsrelationvalue
    extra=1
class FacetsInline(admin.StackedInline):
    model = Facets
    extra=1
    
class   InfoAdmin(admin.ModelAdmin):
    
    inlines = [
        HitsrelationvalueInline,FacetsInline
       
    ]
   
    list_display = ['info_id',
                    
                    'hits',
                    'page',
                    'facets',
                   
                    ]
   
    filter_horizontal = ()
 
 
admin.site.register(Info,InfoAdmin)
