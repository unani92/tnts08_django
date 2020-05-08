from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import JoinMatchForm, JoinForm
from .models import JoinMatch, Join, Dismiss
# Create your views here.

@login_required
def index(request):
    matches = JoinMatch.objects.all()
    paginator = Paginator(matches,4)

    if request.GET.get('search'):
        page = request.GET.get('search')
    else :
        page = request.GET.get('page')

    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage :
        matches = paginator.page(paginator.num_pages)

    idx = matches.number-1
    max_idx = len(paginator.page_range)
    start_idx = idx - 2 if idx >= 2 else 0
    if idx < 2:
        end_idx = 5 - start_idx
    else:
        end_idx = idx + 3 if idx <= max_idx else max_idx

    page_range = list(paginator.page_range[start_idx:end_idx])

    context = {
        'matches':matches,
        'page_range':page_range,
        'max_idx':max_idx,
    }

    return render(request,'calender/index.html',context)

@login_required
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

@login_required
def detail(request,pk):
    match = get_object_or_404(JoinMatch,pk=pk)
    joinform = JoinForm()
    context = {
        'match':match,
        'joinform':joinform,
    }
    return render(request,'calender/detail.html',context)

@login_required
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
            dismiss.delete()

        match.join_match.add(join)
        return response

@login_required
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
            join.delete()

        match.dismiss_match.add(dismiss)
        return response

@login_required
def search(request):
    term = request.GET.get('q')
    matches = JoinMatch.objects.filter(vs__exact=term)
    paginator = Paginator(matches, 4)
    page = request.GET.get('page')

    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)

    idx = matches.number - 1
    max_idx = len(paginator.page_range)
    start_idx = idx - 2 if idx >= 2 else 0
    if idx < 2:
        end_idx = 5 - start_idx
    else:
        end_idx = idx + 3 if idx <= max_idx else max_idx

    page_range = list(paginator.page_range[start_idx:end_idx])

    context = {
        'matches': matches,
        'page_range': page_range,
        'max_idx': max_idx,
    }
    return render(request,'calender/index.html',context)