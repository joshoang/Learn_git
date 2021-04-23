from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    return render(request,'pages/home.html')
def contact(request):
   return render(request, 'pages/contact.html')
def error(request,*args, **kwargs):
   return render(request, 'pages/error.html')


class Logout(View):
    
    def get(self,request):
        form = LoginForm()
        logout()
        return render(request, 'pages/login.html',{'form':form})

class Login(View):
    
    def get(self,request):
        form = LoginForm()
        redirect_url = request.GET.get('next',"/")
        return render(request, 'pages/login.html',{'form':form,'next':redirect_url})

    def post(self,request):
        data_request = request.POST
        form = LoginForm(data_request)
        if form.is_valid():
            my_user  =  authenticate(username = data_request.get('username'),password = data_request.get('password'))
            if my_user is None:
                return render(request, 'pages/login.html',{'form':form,'message':'Mật khẩu không khớp'})
            login(request,my_user)
            return HttpResponseRedirect(data_request.get('next'))    
        return render(request, 'pages/login.html',{'form':form})
def register(request):
    form = RegistrationForm()
    if request.method =="POST" :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html',{'form':form})