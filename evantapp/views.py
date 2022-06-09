from django.shortcuts import render, redirect
from .models import UserMember
from django.contrib.auth.models import User
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def addDetails(request):
    return render(request,'personalise.html')
def add_data(request):
    if  request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        guest=request.POST['guest']
        event=request.POST['event']
        date=request.POST['date']
        budget=request.POST['budget']
        venue=request.POST['venue']
        phone=request.POST['phone']
        discription=request.POST['discription']


        detail=UserMember(
                    user_name=name,
                   user_email=email,
                    user_guest=guest,
                    user_event=event,
                    user_time=date,
                    user_budget=budget,
                    user_venue=venue,
                    user_phone=phone,
                    user_discription=discription
                   )

        detail.save()
        

       
        return redirect ('/')

# login decroter needs to be added
def admin_event_view(request):
    event_list = UserMember.objects.all()
    
    return render(request, 'ad_approve.html', {"event_list": event_list})
#@login_required(login_url='load_loginpage')

def booking_details(request):
    std=UserMember.objects.all()
    return render(request,'ad_show.html',{'std':std})

#Signup view function
def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('login')
	else:
		form = RegisterUserForm()

	return render(request, 'register_user.html', {
		'form':form,
		})

#Login and Logout
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('login')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('home')	


	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')