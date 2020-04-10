from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request) : 
    boards = Board.objects.order_by('-pk')
    context = {'boards':boards}
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