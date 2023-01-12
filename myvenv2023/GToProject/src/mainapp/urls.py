
from django.urls import path


from mainapp.views import (
   search_View,graph_Shaw_View,graph_Shaw_View_Index
)

app_name="mainapp"
urlpatterns = [
  
   path('search', search_View, name='search'),
   path('graph',graph_Shaw_View,name='graph'),
   path('index',graph_Shaw_View_Index,name='index'),
   
]

