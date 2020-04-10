from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request) : 
    boards_list = Board.objects.order_by('-pk')
    paginator = Paginator(boards_list,2)
    page = request.GET.get('page')

    try: 
        boards = paginator.page(page)
    except PageNotAnInteger : 
        boards = paginator.page(1)
    except EmptyPage : 
        boards = paginator.page(paginator.num_pages)

    context = {'boards':boards}

    print(boards.has_other_pages())

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
    return render(request,'board/create.html',context)

def update(request) : 
    pass

def delete(requets) : 
    pass