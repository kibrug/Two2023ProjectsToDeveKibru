from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
import json
from django.db.models import Q



from django.contrib.auth.hashers import make_password
from django.views import View
from account.models import User,FreeAccountUser,CutomeAccountUser
from mainapp.models import Facets,Frequency,Country



from account.models import User
from mainapp.models import Frequency,Category,Facets,Hits
from mainapp.utils import get_plot 
from account.forms import (AccountUpdateForm,AccountAuthenticationForm)
# Json Formats 
def json_View(request):
    #data = list(User.objects.values())
    #data =list(FreeAccountUser.objects.values())
    data =list(Facets.objects.values())
    
    return JsonResponse(data ,safe=False)
def home_View(request):
    countrys = Country.objects.all()
    qsch = Facets.objects.all()
    hitdata = Hits.objects.all()
    qs = Frequency.objects.all()
    qsp = Category.objects.all()
    x =[x.data for x in qs]
    y = [y.doc_count for y in qs ]
    zy = [zy.frequency_id.country for zy in qs ]
    #s =[s.key for s in qsp]
    z = [z.doc_count for z in qs ]
    graphs = get_plot(x,y,z,zy)
    
             
    
    
    return render(request,'index.html',{'graphs':graphs,'countrys':countrys,'qsch':qsch,'hitdata':hitdata})
def signupoption_View(request):
    
    return render(request, 'account/signupoptions.html')
    
    
    
def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect(settings.LOGIN_REDIRECT_URL)

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				if destination:
					if 'next' in request.POST:
						return redirect(request.POST.get('next'))
					else:
						return redirect(destination)
				return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = AccountAuthenticationForm()
	context['form']=form
	return render(request, "account/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect

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
            return redirect ("account:home")
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
            return redirect ("account:login")
           
           
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
      
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone_number = postData.get ('phone_number')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
           
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
            
            return redirect ("account:login")
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
	
	else:
		account = User.objects.get(pk=user_id)
		
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
						"first_name": account.first_name,
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

            
   
       
   
    
    
    
    
    
    