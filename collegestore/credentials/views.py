from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'newpage.html')
        else :
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')



    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email=  request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Usename taken")
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)


                user.save();
                return render(request,'login.html')

        else:
            messages.info(request,"password not match")
            return redirect('Register')
        return redirect('/')

    return render(request,"register.html")
def new(request):
    return render(request,"add.html")
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        phonenum=  request.POST['phonenum']
        messages.info(request, "Order confirmed")


    else:

        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')