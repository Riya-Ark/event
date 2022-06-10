from django.shortcuts import render, redirect
from .models import UserMember1, UserMember
from django.contrib.auth.models import User, auth
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def addDetails(request):
    return render(request,'personalise.html')
def add_data(request):
    if  request.method=='POST':
        name=request.user
        email=request.POST['email']
        guest=request.POST['guest']
        event=request.POST['event']
        date=request.POST['date']
        budget=request.POST['budget']
        venue=request.POST['venue']
        phone=request.POST['phone']
        discription=request.POST['discription']


        detail=UserMember1(
                    user=name,
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
        

       
        return redirect ('user_show_events')

# login decroter needs to be added
def admin_event_view(request):
    event_list = UserMember.objects.all()
    
    return render(request, 'ad_approve.html', {"event_list": event_list})
#@login_required(login_url='load_loginpage')

def booking_details(request):
    std=UserMember.objects.all()
    return render(request,'ad_show.html',{'std':std})

def user_show_events(request):
    applied = UserMember1.objects.filter(user=request.user)
    users= UserMember.objects.filter(user=request.user)
    context={'applied':applied,'users':users}
    return render(request,'user-show-events.html',context)

def register(request):
    return render(request,'register_user.html')

#User registration
def register_user(request):
    if request.method =='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        # address=request.POST.get('address')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        cpassw=request.POST.get('cpassw')
        
        if cpassw==passw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This Username is already taken!!!')
                return redirect('login_user')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This Email is already taken!!!')
                return redirect('login_user')
            else:
                user = User.objects.create_user(first_name=fname,
                                                     last_name=lname,
                                                     email=email,
                                                     username=uname,
                                                     password=passw)
                user.save()
                u=User.objects.get(id=user.id)
                member=UserMember(
                    # user_address=address,
                                      user=u,
                                      )
                member.save()
                return redirect('load_loginpage')
    
    return redirect('register')

def load_loginpage(request):
    return render(request,'login.html')




#Login and Logout
def login_user(request):
    if request.method =='POST':
        try:
            username = request.POST['uname']
            password = request.POST['passw']
            user = auth.authenticate(username=username,password=password)
            request.session["uid"]=user.id
            if user is not None:
                if user.is_staff:
                    login(request,user)
                    return redirect('welcomeadmin')
                else:
                    login(request,user)
                    auth.login(request,user)
                    # messages.info(request,f'Welcome { username }')
                    return redirect('addDetails')
            else:
                messages.info(request,'invalid username or password.Try again!')
                return redirect('login_user')
        except:
            messages.info(request,'invalid username or password.Try again!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')    




def logout_user(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('login_user')

def welcomeadmin(request):
    return render(request,'adhome.html') 


@login_required(login_url='login_user')
def admin_event_details(request):
    std=UserMember1.objects.all()
    return render(request,'admin-eventtable.html',{'std':std})



def load_leave_requests(request):
    users = UserMember1.objects.all().filter(status="0")
    return render(request, 'load_leave_requests.html',{'users':users})
def aprove_leave_req(request):
    aproved = UserMember1.objects.all().filter(status="1")
    return render(request,'aprove_leave.html',{'aproved':aproved})

def rejected_leave_req(request):
    rejected = UserMember1.objects.all().filter(status="2")
    return render(request,'rejected_leave.html',{'rejected':rejected})

def aprove_event(request,  pk):
    leaveStatus = UserMember1.objects.get(id=pk)
    leaveStatus.status = "1"
    leaveStatus.save()
    return redirect('admin_event_details')
def reject_event(request, pk):
    leaveStatus = UserMember1.objects.get(id=pk)
    leaveStatus.status = "2"
    leaveStatus.save()
    return redirect('admin_event_details')


