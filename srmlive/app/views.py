from django.shortcuts import render,redirect
from.models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request,'admin_dashboard.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request,'invalid user')
            return redirect('login')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def create_admin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        admin=Create_Admin.objects.create(username=username,email=email,password=password)
        # print(admin)
        admin.save()
        return redirect('list')
    return render(request,'create_admin.html')

def admin_list(request):
    admins=Create_Admin.objects.all()
    return render(request,'admin_list.html',{'admins_list':admins})

def delete_admin(request,id):
    admins=Create_Admin.objects.get(id=id)
    admins.delete()
    return redirect('list')

# def edit_admin(request,id):
#     admins=Create_Admin.objects.get(id=id)
#     if request.method=='POST':
        

