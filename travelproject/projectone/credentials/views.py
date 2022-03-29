from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        un=request.POST['uname']
        pw=request.POST['pass']
        user=auth.authenticate(username=un,password=pw,)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['firstname']
        c = request.POST['lastname']
        d = request.POST['email']
        e = request.POST['pass']
        f = request.POST['cpass']
        if e==f:
            if User.objects.filter(username=a):
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=d):
                messages.info(request,"Email id taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=a,password=e,first_name=b,last_name=c,email=d)
                user.save();
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password not Matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register1.html")