from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView

from mainapp.models import Frequency,Category
from mainapp.utils import get_plot 



# Create your views here.



def search_View(request):  # new
    query = request.GET.get("q")
    data_list = Frequency.objects.filter(
            Q(key__icontains=query) | Q(doc_count__icontains=query)
        )
    context={"data_list": data_list}
    return render(request, "search_results.html", context)


def graph_Shaw_View(request):
    #x=[3,1,5]
    #y=[20,8,23]
    qs = Frequency.objects.all()
    qsp = Category.objects.all()
    x =[x.key for x in qsp]
    y = [y.doc_count for y in qsp ]
    #s =[s.key for s in qsp]
    z = [z.doc_count for z in qs ]
    chart = get_plot(x,y,z)
    return render(request,'graph.html',{'chart':chart})

def graph_Shaw_View_Index(request):
     #x=[3,1,5]
    #y=[20,8,23]
    qs = Frequency.objects.all()
    qsp = Category.objects.all()
    x =[x.key for x in qsp]
    y = [y.doc_count for y in qsp ]
    #s =[s.key for s in qsp]
    z = [z.doc_count for z in qs ]
    graphs = get_plot(x,y,z)
    return render(request,'index.html',{'graphs':graphs})


        
