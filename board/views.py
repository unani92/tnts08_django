from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Board, Hashtag, Hit, Reply
from .forms import BoardForm, CommentForm, ReplyForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.db.models import Q

# Create your views here.
@login_required
def index(request) :
    notices = Board.objects.filter(choice='공지').order_by('-pk')
    boards_list = Board.objects.filter(choice='일반').order_by('-pk')
    paginator = Paginator(boards_list,4)

    if request.GET.get('search'):
        page = request.GET.get('search')
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
        'notices':notices,
        'boards':boards,
        'page_range':page_range,
        'max_idx':max_idx-2,
        }

    return render(request, 'board/index.html', context)

@login_required
def create(request) : 
    if request.method == "POST" : 
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            hit = Hit()
            hit.board = board
            hit.save()
            board.name=request.user.first_name
            board.save()

            # hashtag
            hashtag = Hashtag()
            hashtag.content = board.hashtag
            hashtag.save()
            hashtag.board.add(board)

            messages.success(request,'새 글이 등록되었습니다.')

            return redirect('board:detail',board.pk)
    else : 
        form = BoardForm()
    context = {'form':form}
    return render(request,'board/form.html',context)

@login_required
def detail(request,pk) : 
    board = get_object_or_404(Board,pk=pk)
    commentform = CommentForm()
    replyform = ReplyForm()

    if board.hashtag_boards.all():
        hashtag = board.hashtag_boards.all()[0]
        hash_list = hashtag.content.split('#')
        hash_list = hash_list[1:]
        context = {
            'board': board,
            'hash_list': hash_list,
            'commentform': commentform,
            'replyform':replyform,
        }
    else :
        context = {
            'board':board,
            'commentform':commentform,
            'replyform':replyform,
        }
    response = render(request,'board/detail.html',context)
    cookie_name = f'hit:{request.user.username}'

    # Cookie
    if request.COOKIES.get(cookie_name) :
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(pk) not in cookies_list:
            response.set_cookie(cookie_name,cookies+f'|{pk}',expires=7200)
            hit = board.hit_set.all()[0]
            hit.count += 1
            hit.save()
            return response

    else :
        response.set_cookie(cookie_name,pk,expires=7200)
        hit = board.hit_set.all()[0]
        hit.count += 1
        hit.save()
        return response

    return render(request,'board/detail.html',context)    

@login_required
def update(request,pk) : 
    board = get_object_or_404(Board,pk=pk)
    if request.method=='POST' : 
        form = BoardForm(request.POST,instance=board)
        if form.is_valid(): 
            board = form.save()

            # hashtag
            hashtag = board.hashtag_boards.all()[0]
            hashtag.content = board.hashtag
            hashtag.save()

            messages.success(request,'게시글이 수정되었습니다.')
            return redirect('board:index')

    else :
        if board.name == request.user.first_name :
            form=BoardForm(instance=board)
        else :
            return redirect('board:index')
    context = {'form':form}
    return render(request,'board/form.html',context)

@login_required
@require_POST
def delete(requets,pk) : 
    board = get_object_or_404(Board,pk=pk)
    board.delete()
    return redirect('board:index')

@login_required
def CommentCreate(request,board_pk):
    board = get_object_or_404(Board,pk=board_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.name = request.user
        comment.board = board
        board.updated_at = datetime.now()

        comment.save()
        board.save()
        return redirect('board:detail',board.pk)

@login_required
def CommentDelete(request,board_pk,comment_pk):
    board = get_object_or_404(Board,pk=board_pk)
    comment = board.comment_set.get(pk=comment_pk)
    comment.delete()
    return redirect('board:detail',board_pk)

def search(request):
    keyword = request.GET.get('keyword')
    if request.GET.get('choose') == 'title':
        boards = Board.objects.filter(title__contains=keyword)
    elif request.GET.get('choose') == 'name':
        boards = Board.objects.filter(name__exact=keyword)
    else :
        boards = Board.objects.filter(content__contains=keyword)

    context = {'boards':boards}

    return render(request,'board/index.html',context)

def like(request,pk):
    board = get_object_or_404(Board,pk=pk)
    if request.user not in board.like_users.all() and request.user not in board.dislike_users.all():
        board.like_users.add(request.user)
    else :
        board.dislike_users.remove(request.user)
        board.like_users.add(request.user)
    return redirect('board:detail', board.pk)

def dislike(request,pk):
    board = get_object_or_404(Board,pk=pk)
    if request.user not in board.like_users.all() and request.user not in board.dislike_users.all():
        board.dislike_users.add(request.user)
    else :
        board.like_users.remove(request.user)
        board.dislike_users.add(request.user)
    return redirect('board:detail',board.pk)

def search_tag(request):
    term = request.GET.get('term')
    boards = Board.objects.filter(Q(title__contains=term) | Q(content__contains=term))
    context = {'boards':boards}
    return render(request,'board/index.html',context)

def ReplyCreate(request,board_pk,comment_pk):
    board = get_object_or_404(Board,pk=board_pk)
    comment = board.comment_set.get(pk=comment_pk)
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.name = request.user
            reply.comment = comment
            board.updated_at = datetime.now()

            reply.save()
            board.save()
            return redirect('board:detail', board.pk)

def ReplyDelete(request,board_pk,reply_pk):
    reply = get_object_or_404(Reply,pk=reply_pk)
    if request.user == reply.name:
        reply.delete()
        return redirect('board:detail',board_pk)

    else :
        return redirect('board:detail',board_pk)