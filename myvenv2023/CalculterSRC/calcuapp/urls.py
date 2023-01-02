from django.urls import path

from calcuapp.views import index_View


urlpatterns = [
    path('',index_View,name='index'),
]
