from django.urls import path
from . import views
app_name = 'calender'
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create,name='create'),
    path('<int:pk>/', views.detail,name='detail'),
    path('<int:pk>/joinmatch/',views.joinmatch,name='joinmatch'),
    path('<int:pk>/dismiss/',views.dismiss,name='dismiss'),
    path('search/', views.search, name='search')
]