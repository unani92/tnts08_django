from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request) : 
    boards_list = Board.objects.order_by('-pk')
    paginator = Paginator(boards_list,2)

    if request.method == "POST" : 
        page = request.POST.get('search')    
    else : 
        page = request.GET.get('page')

    try: 
        boards = paginator.page(page)
    except PageNotAnInteger : 
        boards = paginator.page(1)
    except EmptyPage : 
        boards = paginator.page(paginator.num_pages)

    idx = boards.number-1
    max_idx = len(paginator.page_range)
    start_idx = idx-2 if idx >= 2 else 0
    if idx < 2 : 
        end_idx = 5-start_idx
    else : 
        end_idx = idx+3 if idx <= max_idx else max_idx
    
    page_range = list(paginator.page_range[start_idx:end_idx])

    context = {
        'boards':boards,
        'page_range':page_range,
        'max_idx':max_idx-2,
        }

    return render(request, 'board/index.html', context)

def create(request) : 
    if request.method == "POST" : 
        form = BoardForm(request.POST)    
        if form.is_valid():
            board = form.save()
            return redirect('board:index')
    else : 
        form = BoardForm()
    context = {'form':form}
    return render(request,'board/form.html',context)

def detail(request,pk) : 
    board = get_object_or_404(Board,pk=pk)
    context = {'board':board}
    return render(request,'board/detail.html',context)    

def update(request,pk) : 
    board = get_object_or_404(Board,pk=pk)
    if request.method=='POST' : 
        form = BoardForm(request.POST,instance=board)
        if form.is_valid(): 
            board = form.save()
            return redirect('board:index')

    else : 
        form=BoardForm(instance=board)
    context = {'form':form}
    return render(request,'board/form.html',context)

@require_POST
def delete(requets,pk) : 
    board = get_object_or_404(Board,pk=pk)
    board.delete()
    return redirect('board:index')
