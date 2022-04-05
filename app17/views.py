from django.contrib.messages.api import success
from django.shortcuts import render,redirect
from . models import Signup
from . forms import SignupForm,LoginForm,ChangePasswordForm
from . forms import UpdateForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.

def index(request):
    any='django'
    return render(request,'index.html',{'next':any})
def register(request):
    if request.method=='POST':
        f=SignupForm(request.POST or None,request.FILES or None)
        if f.is_valid():
            name=f.cleaned_data["Name"]
            age=f.cleaned_data["Age"]
            place=f.cleaned_data["Place"]
            photo=f.cleaned_data["Photo"]
            email=f.cleaned_data["Email"]
            password=f.cleaned_data["Password"]
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"email already exist")
                return redirect('/register')
            else:
                tab=Signup(Name=name,Age=age,Email=email,Place=place,Photo=photo,Password=password)
                tab.save()
                messages.success(request,"registration successful")
                return redirect('/')
        
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})
def login(request):
    if request.method=='POST':
        f=LoginForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data["Email"]
            password=f.cleaned_data["Password"]
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"email does not exist")
                return redirect('login/')
            elif user.Password !=password:
                messages.warning(request,"incorrect password")
                return redirect('login/')
            else:
                messages.success(request,"login success")
                return redirect('/home/%s' % user.id)
    else:
        f=LoginForm()
    return render(request,'login.html',{'form':f})


def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,"home.html",{'user':user})
def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            name=form.cleaned_data["Name"]
            age=form.cleaned_data["Age"]
            email=form.cleaned_data["Email"]
            place=form.cleaned_data["Place"]
            form.save()
            messages.success(request,"updated successfully")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'signup.html',{'form':form,'user':user})
def passwordchange(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data["OldPassword"]
            newpassword=form.cleaned_data["NewPassword"]
            confirmpassword=form.cleaned_data["ConfirmPassword"]
            if user.Password != oldpassword:
                messages.warning(request,"incorrect password")
                return redirect('/passwordchange/%s' % user.id)
            elif newpassword != confirmpassword:
                messages.warning(request,"password mismatch")  
                return redirect('/passwordchange/%s' % user.id) 
            else:
                user.Password= newpassword
                user.save() 
                messages.success(request,"success") 
                return redirect('/home/%s' % user.id) 
    else:
          form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form})
def logout(request):
    logouts(request)
    messages.success(request,"logout successfully")
    return redirect('/')

            
    

        
        
    
    