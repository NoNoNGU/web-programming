from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)

            return redirect('home')
          
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html',{'user':user})           
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")
    
def home(request):
    user = request.username
    return render(request, 'home.html',{'user':user})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # redirect('home')
    return render(request,'login.html')

def user_information(request):
    print(request.user.username)
    # test
    print(request.user.email)
    # test@yahoo.co.jp
    print(request.user.is_active)
    # True
    print(request.user.is_staff)
    # False
    print(request.user.is_superuser)
    # False