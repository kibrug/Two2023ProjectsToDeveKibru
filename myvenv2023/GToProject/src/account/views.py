from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
from account.models import User


#from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View
from account.models import User,FreeAccountUser,CutomeAccountUser
from mainapp.models import Facets,Frequency

from django.http import JsonResponse
import json
from django.db.models import Q


from mainapp.models import Frequency,Category
from mainapp.utils import get_plot 
from account.forms import (AccountUpdateForm)
# Json Formats 
def json_View(request):
    #data = list(User.objects.values())
    #data =list(FreeAccountUser.objects.values())
    data =list(Facets.objects.values())
    
    return JsonResponse(data ,safe=False)
def home_View(request):
    qs = Frequency.objects.all()
    qsp = Category.objects.all()
    x =[x.key for x in qsp]
    y = [y.doc_count for y in qsp ]
    #s =[s.key for s in qsp]
    z = [z.doc_count for z in qs ]
    graphs = get_plot(x,y,z)
    
    return render(request,'index.html',{'graphs':graphs})
def signupoption_View(request):
    
    return render(request, 'signupoptions.html')
    

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        user = User.get_user_by_email (email)
        error_message = None
        if user:
            flag = check_password (password, user.password)
            if flag:
                request.session['user'] = user.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect (settings.LOGOUT_REDIRECT_URL)
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'login.html', {'error': error_message})

def logout_View(request):
    request.session.clear()
    return redirect(settings.LOGOUT_REDIRECT_URL)

class Signup (View):
    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username = postData.get ('username')
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone_number = postData.get ('phone_number')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'username':username,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        error_message = None

        user = User (
                             
                             first_name=first_name,
                             last_name=last_name,
                             phone_number=phone_number,
                             email=email,
                             password=password)
        error_message = self.validateUser (user)

        if not error_message:
            print ( first_name, last_name, phone_number, email, password)
            user.password = make_password(user.password)
            user.save()
            return redirect ('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateUser(self, user):
        error_message = None
       
        if (not user.first_name):
            error_message = 'Please Enter your First Name'
        elif len (user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not user.phone_number:
            error_message = 'Enter your Phone Number'
        elif len (user.phone_number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
class Signup_Free_Account_User(View):
    def get(self, request):
        return render (request, 'free_account_user.html')

    def post(self, request):
        postData = request.POST
        #username = postData.get ('username')
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone_number = postData.get ('phone_number')
        email = postData.get ('email')
        password = postData.get ('password')
        print(first_name)
        print(last_name)
        print(phone_number)
        print(email)
        # validation
        value = {
            #'username':username,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        error_message = None

        user = FreeAccountUser (
                             free_user = True,
                             first_name=first_name,
                             last_name=last_name,
                             phone_number=phone_number,
                             email=email,
                             password=password)
        error_message = self.validateUser (user)
        #user.save()

        if not error_message:
            print ( first_name, last_name, phone_number, email, password)
            user.password = make_password(user.password)
            user.register()
            return redirect ('home')
           
           
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'free_account_user.html', data)

    def validateUser(self, user):
        error_message = None
       
        if (not user.first_name):
            error_message = 'Please Enter your First Name'
        elif len (user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not user.phone_number:
            error_message = 'Enter your Phone Number'
        elif len (user.phone_number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
    
class Signup_Custome_Account_User(View):
    def get(self, request):
        return render (request, 'custome_account_user.html')

    def post(self, request):
        postData = request.POST
        #username = postData.get ('username')
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone_number = postData.get ('phone_number')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            #'username':username,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        error_message = None

        user = CutomeAccountUser(
                             custome_user=True,
                             first_name=first_name,
                             last_name=last_name,
                             phone_number=phone_number,
                             email=email,
                             password=password)
        error_message = self.validateUser (user)
        #user.save()

        if not error_message:
            print ( first_name, last_name, phone_number, email, password)
            user.password = make_password(user.password)
            user.register ()
            
            return redirect ('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'custome_account_user.html', data)

    def validateUser(self, user):
        error_message = None
       
        if (not user.first_name):
            error_message = 'Please Enter your First Name'
        elif len (user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not user.phone_number:
            error_message = 'Enter your Phone Number'
        elif len (user.phone_number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
    
    
# profile views
@login_required
def profile_View(request, *args, **kwargs):
    user_id = request.user.id 
    
    if not request.user.is_authenticated: 
        return redirect(settings.LOGIN_URL)
    else:
        account=User.objects.get(id=user_id)
        context={'account':account,
                 }
        return render(request, 'account/profile.html',context)   
    
    
@login_required
def edit_account_view(request, *args, **kwargs):
	user_id = request.user.id 
 
	if not request.user.is_authenticated:
		return redirect("account:login")
	#user_id = kwargs.get("user_id")
	else:
		account = User.objects.get(pk=user_id)
		#worker  = Worker.objects.get(user_id=user_id)
		if account.pk != request.user.pk:
			return HttpResponse("You cannot edit someone elses profile.")
		context = {}
		if request.POST:
			form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
			if form.is_valid():
				form.save()
				return redirect("account:profile")
			else:
				form = AccountUpdateForm(request.POST, instance=request.user,
					initial={
						
						"email": account.email, 
						"profile_imag":account.profile_imag,
						"frist_name": account.frist_name,
						"last_name": account.last_name,
						
						"phone_number": account.phone_number,
						
					}
				)
				context['form'] = form
		else:
			form = AccountUpdateForm(
				initial={
						"id": account.pk,
						"email": account.email, 
						"profile_imag":account.profile_imag,
						"first_name": account.first_name,
						"last_name": account.last_name,
						
						"phone_number": account.phone_number,
						
					}
				)
			context['form'] = form
		
		return render(request, "account/edit_account.html", context)

            
   
       
   
    
    
    
    
    
    