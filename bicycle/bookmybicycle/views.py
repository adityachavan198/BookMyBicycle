# from django.shortcuts import render
from django.http import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import json

# Create your views here.
def index(request):
    context= {
        'UsersOfApp': UserOfApp.objects.all()
        # 'cycles': Cycle.objects.all()
        # 'stands': Stand.objects.all()
        # 'logs': Log.objects.all()
    }

    return render(request, "bookmybicycle/index.html", context)

def log_me_out(request):
    logout(request)
    return render(request, "bookmybicycle/index.html", {})

def booking(request):
        if not request.user.is_authenticated:
            return render(request, "bookmybicycle/login.html",{"message": "You need to Log In first!"})
        context={
            "user": request.user
        }
        # return render(request,

def book_bicycle(request):
    print(request.POST)
    from_date,from_time,from_city = request.POST['from_date'],request.POST['from_time'],request.POST['from_city']
    from_state,from_location = request.POST['from_state'],request.POST['from_location']
#    from_sid = using state city loc

    to_date,to_time,to_city = request.POST['to_date'],request.POST['to_time'],request.POST['to_city']
    to_state,to_location = request.POST['to_state'],request.POST['to_location']
#   to_sid

    print(request.POST)
    return HttpResponseRedirect(reverse('trialpage'))

def login_r(request):
    return render(request, 'bookmybicycle/login.html', {})

def trialpage(request):
    states = Stand.objects.values('sstate')
    states = [x['sstate'] for x in states]
    # states.append("")
    states=list(set(states))
    states.sort()
    print(states)
    return render(request, 'bookmybicycle/User_Pages/Home_trial.html',{ 'states' : states})

def get_city(request):
    state_name = request.GET['state']

    result_set = []

    answer = str(state_name[1:-1])
    selected_cities = Stand.objects.filter(sstate=answer).values('scity').distinct()
    for city in selected_cities:
        result_set.append(city)
    return HttpResponse(json.dumps(result_set), content_type='application/json')


def get_loc(request):
    city_name = request.GET['city']
    city_name = str(city_name)

    state_name = request.GET['state']
    state_name = str(state_name[1:-1])


    result_set = []
    selected_loc = Stand.objects.filter(sstate=state_name,scity=city_name).values('sloc').distinct()
    for loc in selected_loc:
        result_set.append(loc)
    return HttpResponse(json.dumps(result_set), content_type='application/json')

# def my_login(request):
#     eemail = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, email=eemail, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         return render(request, 'bookmybicycle/home.html', {})
#
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, HttpResponse('Invalid'))

# def authenticate(request):
#     username = request.POST['email']
#     l = User.objects.filter(username=username)
#     if len(l):
#         request.session['username'] = username
#         return HttpResponseRedirect(reverse("HomePage"))
#     else:
#         return HttpResponseRedirect(reverse("login"))

def my_login(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    # return redirect('welcomeuser.html')
        return render(request, 'bookmybicycle/welcomeuser.html', {})
    else:
        return render(request, 'bookmybicycle/login.html', {'loginfail' : True })

def home(request):
    userid = request.POST['email']
    request.session['email'] = userid
    x = {
        'email' : request.session['email']
        }
    return render(request,'bookmybicycle/home.html', x)

def register(request):
    return render(request, 'bookmybicycle/register.html', {})

def my_register(request):
    username = request.POST['email']
    password = request.POST['password']
    uaddr = request.POST['address']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    state = request.POST['state']
    city = request.POST['city']
    phone = request.POST['phone']
    zip = request.POST['zip']
    user = UserOfApp.objects.create_user(username=username, email=username, password=password,
    uaddr=uaddr, first_name=first_name, last_name=last_name, state=state, city=city, phone=phone, zip=zip)
    user.save()
    return render(request, 'bookmybicycle/register.html', {'registered' : True})

def signup(request):
    username = request.POST['email']
    password = request.POST['password']
    uaddr = request.POST['address']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    state = request.POST['state']
    city = request.POST['city']
    phone = request.POST['phone']
    zip = request.POST['zip']
    user = UserOfApp.objects.create_user(username=username, email=username, password=password,
    uaddr=uaddr, first_name=first_name, last_name=last_name, state=state, city=city, phone=phone, zip=zip)

    user.is_active = False
    user.save()
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message = render_to_string('bookmybicycle/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token':account_activation_token.make_token(user),
    })
    to_email = username
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()
    return render(request, 'bookmybicycle/login.html',{'registered' : True})

def profile(request):
    return render(request, 'bookmybicycle/profile.html')

def delete_user(request):
    pass
#     user=request.user.username
#     u = User.objects.get(username = user)
#     user.
#     u.delete()
#     return render(request, 'bookmybicycle/index.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserOfApp.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserOfApp.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return render(request,'bookmybicycle/reg_success.html')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
