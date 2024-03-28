from django.shortcuts import render

# Create your views here.


def index_View(request):
    
    return render(request,'index.html')
