from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            # return redirect('login')


    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        usernme=request.POST["username"]
        fstnme = request.POST["first_name"]
        lastnme = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        pass2 = request.POST["confirm password"]
        if password==pass2:
            if User.objects.filter(username=usernme).exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            user=User.objects.create_user(username=usernme,first_name=fstnme,last_name=lastnme,email=email)
            user.save()
            return redirect('login')
            print("user created")
        else:
            messages.info(request, "password is not matched")
            return redirect('register')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
