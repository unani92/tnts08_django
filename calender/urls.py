from django.urls import path
from . import views
app_name = 'calender'
urlpatterns = [
    path('create/',views.create,name='create'),
    path('<int:pk>/', views.detail,name='detail'),
    path('<int:pk>/joinmatch/',views.joinmatch,name='joinmatch'),
]