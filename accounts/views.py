from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from .models import MyUser
# Create your views here.

def signup(request) : 
    
    if request.method == 'POST' : 
        form = MyUserCreationForm(request.POST)
        if form.is_valid() and request.POST.get('agree1') and request.POST.get('agree2'): 
            form.save()
            return redirect('board:index')
    else : 
        form = MyUserCreationForm()
    context = {'form':form}

    return render(request,'accounts/signup.html',context)

def detail(request) : 
    if request.GET.get('firstname') : 
        search = request.GET.get('firstname')
        users = MyUser.objects.filter(first_name=search)
    
    else : 
        users = MyUser.objects.order_by('first_name')

    context = {'users':users}
    return render(request,'accounts/detail.html',context)
