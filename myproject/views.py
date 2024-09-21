from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from myapp.models import *

def loginpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password = req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login (req,user)
            return redirect('homepage')


    return render(req, 'login.html')

def registerpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        password = req.POST.get('password')
        Confirm_Password=req.POST.get('Confirm_Password')

        if password==Confirm_Password:
            user=User.objects.create_user(username=username,email=email,password=Confirm_Password)
            return redirect('loginpage')

        else:
            return HttpResponse('Password not Matched')


    return render(req, 'register.html')

@login_required
def homepage(req):
    return render(req,'home.html')

def logoutpage(req):
    logout(req)
    return redirect('homepage')

def base(req):
    return render(req,'base.html')

@login_required
def dashboard(req):
    return render(req,'dashboard.html')

@login_required
def contact(req):
    return render(req,'contact.html')

@login_required
def jobdetail(req):
    return render(req,'job-detail.html')

@login_required
def job_table(req):
    data=jobmodel.objects.all()
    return render(req,'jobtable.html',{'data':data})

@login_required
def addjob(req):
    if req. method=='POST':
        type=req.POST.get('type')
        description=req.POST.get('description')
        logopic=req.FILES.get('logopic')
        location=req.POST.get('location')
        selary=req.POST.get('selary')

        job=jobmodel(
            type=type,
            description=description,
            logopic=logopic,
            location=location,
            selary=selary,
        )
        job.save()
    
    return render(req,'addjob.html')

@login_required
def singlejob(req,id):
    data=jobmodel.objects.filter(id=id)
    return render(req,'singlepage.html',{'data':data})

def edit(req,id):
    data=jobmodel.objects.filter(id=id)
    return render(req,'edit.html',{'data':data})

def update(req):
    if req. method=='POST':
        id=req.POST.get('id')
        type=req.POST.get('type')
        description=req.POST.get('description')
        llogopic=req.FILES.get('loogopic')
        location=req.POST.get('location')
        selary=req.POST.get('selary')
        oldpic=req.POST.get('oldpic')

        job=jobmodel(
            id=id,
            type=type,
            description=description,
            location=location,
            selary=selary,
        )
        if llogopic:
            job.logopic=llogopic
            job.save()
        else:
            job.logopic=oldpic
            job.save()
    
    return redirect('job_table')

def delete(req,id):
    data=jobmodel.objects.filter(id=id)
    data.delete()
    return redirect('job_table')
