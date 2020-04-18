from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, MyAuthenticationForm, MyUserChangeForm
from .models import MyUser
# Create your views here.

def signup(request) : 
    if request.user.is_authenticated:
        return redirect('board:index')

    if request.method == 'POST' : 
        form = MyUserCreationForm(request.POST)
        if form.is_valid() and request.POST.get('agree1') and request.POST.get('agree2'): 
            form.save()
            return redirect('board:index')
    else : 
        form = MyUserCreationForm()
    context = {'form':form}

    return render(request,'accounts/signup.html',context)

@login_required
def detail(request) : 
    if request.GET.get('firstname') : 
        search = request.GET.get('firstname')
        users = MyUser.objects.filter(first_name=search)
    
    else : 
        users = MyUser.objects.order_by('first_name')

    context = {'users':users}
    return render(request,'accounts/detail.html',context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('board:index')

    if request.method == 'POST' : 
        form = MyAuthenticationForm(request,request.POST)
        if form.is_valid() : 
            login(request,form.get_user())
            return redirect(request.GET.get('next') or 'board:index')
    else : 
        form = MyAuthenticationForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)

@login_required
def log_out(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def delete(request) :
    request.user.delete()
    return redirect('/home/')

@login_required()
def update(request) :
    user = MyUser.objects.get(username=request.user.username)
    if request.method=='POST' :
        form = MyUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect('accounts:detail')
    else :
        form = MyUserChangeForm(instance=user)
    context = {'form':form}
    return render(request,'accounts/update.html',context)

