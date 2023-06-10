
from django.urls import path


from mainapp.views import (
   search_View,
)

app_name="mainapp"
urlpatterns = [
  
   path('search', search_View, name='search'),
 
  
   
]

