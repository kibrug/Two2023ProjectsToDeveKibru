from django.shortcuts import render,redirect
from django.db.models import Q
from django.views.generic.list import ListView

from mainapp.models import Frequency,Category,Country,Hits,Facets

from mainapp.utils import get_plot 


def search_View(request):  # new
    query = request.GET.get("q")
    data_list = Hits.objects.filter(
            Q(country__icontains=query) | Q(category__icontains=query) | Q(currency__icontains=query) | Q(importance__icontains=query)| Q(type__icontains=query)| Q(group__icontains=query)| Q(pretty_name__icontains=query)
        )
    context={"data_list": data_list}
    return render(request, "search_results.html", context)





        
   
    
    
    
    
    
    


