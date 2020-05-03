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


# 참전 불참 중복 방지 기능 추가
# 참전 인원 공유하는 드롭다운 개설
    
def joinmatch(request,pk):
    match = get_object_or_404(JoinMatch,pk=pk)
    join = Join()
    join.user = request.user
    join.time = request.POST.get('time')
    join.save()
    match.join_match.add(join)
    return redirect('calender:detail',pk)

def dismiss(request,pk):
    match = get_object_or_404(JoinMatch,pk=pk)
    dismiss = Dismiss()
    dismiss.user = request.user
    dismiss.save()
    match.dismiss_match.add(dismiss)
    return redirect('calender:detail',pk)