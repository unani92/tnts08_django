from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
# Create your views here.

def signup(request) : 
    
    if request.method == 'POST' : 
        form = MyUserCreationForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('board:index')
    else : 
        form = MyUserCreationForm()
    context = {'form':form}

    return render(request,'accounts/signup.html',context)