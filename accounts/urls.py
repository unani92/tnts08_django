from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    path('detail/', views.detail, name='detail'),
    path('login/', views.signin, name='login'),
]
