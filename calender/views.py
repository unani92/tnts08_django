from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import JoinMatchForm, JoinForm
from .models import JoinMatch, Join, Dismiss
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = JoinMatchForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST.get('date'))
            return redirect('board:index')
    else :
        form = JoinMatchForm()
    context = {
        'form':form
    }
    return render(request,'calender/form.html',context)

def detail(request,pk):
    match = get_object_or_404(JoinMatch,pk=pk)
    joinform = JoinForm()
    context = {
        'match':match,
        'joinform':joinform,
    }
    return render(request,'calender/detail.html',context)


# 참전 인원 공유하는 드롭다운 개설
    
def joinmatch(request,pk):
    response = redirect('calender:detail', pk)
    match = get_object_or_404(JoinMatch,pk=pk)
    if match.join_match.filter(user=request.user):
        return response
    else :
        join = Join()
        join.user = request.user
        join.time = request.POST.get('time')
        join.save()

        if match.dismiss_match.filter(user=request.user):
            dismiss = match.dismiss_match.get(user=request.user)
            match.dismiss_match.remove(dismiss)

        match.join_match.add(join)
        return response

def dismiss(request,pk):
    response = redirect('calender:detail', pk)
    match = get_object_or_404(JoinMatch,pk=pk)
    if match.dismiss_match.filter(user=request.user):
        return response
    else :
        dismiss = Dismiss()
        dismiss.user = request.user
        dismiss.save()

        if match.join_match.filter(user=request.user):
            join = match.join_match.get(user=request.user)
            match.join_match.remove(join)

        match.dismiss_match.add(dismiss)
        return response