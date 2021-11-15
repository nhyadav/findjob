from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Employee,Employer
from django.views import View
# Create your views here.
def home(request):
    return render(request, 'home/index.html')


class MySignupView(View):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'home/signup.html'
    def get(self, request,*args, **kwargs):
        return render(request, 'home/signup.html')
    def post(self, request, *args, **kwargs):   
        if request.method == 'POST':
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            re_password = request.POST['repsw']
            city = request.POST['city']
            country = request.POST['country']  
            role = request.POST['role']
            
            emp = Employee(firstname=firstname, lastname=lastname, email=email, city=city, country=country, role=role )
        
            emp.save()
            print('Done ..................')
        return render(request, 'home\login.html')
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'home/login.html'