from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.MyLoginView.as_view()),
    path('signup', views.MySignupView.as_view()),
    
]
