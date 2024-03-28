
from django.urls import path

from account.views import (home_View,Signup,
                           Login,logout_View,
                           Signup_Free_Account_User,
                           Signup_Custome_Account_User,
                           json_View,
                           signupoption_View,
                           profile_View,
                           edit_account_view)
from django.conf import settings
app_name="account"
urlpatterns = [
   path('',home_View, name='home'),
   path('json',json_View,name='json'),
   path('signup', Signup.as_view(), name='signup'),
   path('signupoption',signupoption_View,name='signupoption'),
   path('login', Login.as_view(), name='login'),
   path('logout',logout_View,name='logout'),
   path('free_account',Signup_Free_Account_User.as_view(),name='free_account'),
   path('custome_account',Signup_Custome_Account_User.as_view(),name='custome_account'),
   path('profile',profile_View,name='profile'),
   path('edit',edit_account_view,name='edit'),
]

