from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/',views.detail, name='detail'),
    path('<int:pk>/update',views.update, name='update'),
    path('<int:pk>/delete',views.delete, name='delete'),
    path('search/',views.search, name='search'),
    path('<int:board_pk>/comment/', views.CommentCreate, name='comment_create'),
    path('<int:board_pk>/<int:comment_pk>/comment/', views.ReplyCreate, name='reply_create'),
    path('<int:board_pk>/<int:reply_pk>/reply/delete/', views.ReplyDelete, name='reply_delete'),
    path('<int:board_pk>/<int:comment_pk>/delete/', views.CommentDelete, name='comment_delete'),
    path('<int:pk>/like', views.like, name='like'),
    path('<int:pk>/dislike', views.dislike, name='dislike'),
    path('search_tag/', views.search_tag, name='search_tag'),
    path('<int:board_pk>/<int:comment_pk>/CommentLike/', views.CommentLike, name='comment_like'),
    path('<int:board_pk>/<int:comment_pk>/CommentDisike/', views.CommentDislike, name='comment_dislike'),
    path('<int:pk>/CommentSort/', views.CommentSort,name='CommentSort'),
]
