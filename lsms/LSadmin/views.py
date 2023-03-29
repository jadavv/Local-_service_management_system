from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
# from .forms import ServiceProviderRegisterForm,CustomerRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.



class AdminLoginView(LoginView):
    template_name= 'LSadmin/login.html'
    success_url ="/"
    
    # def get_redirect_url(self):
    #     if self.request.user.is_authenticated:
    #         if self.request.user.is_servicer:
    #             return '/Uapp/DashboardView/'
    #         else:
    #             return '/Uapp/DashboardView/'
            
    
class Dashboardmanage(TemplateView):
    template_name = 'LSadmin/dashboard.html'
    
class Sidebarmanage(TemplateView):
    template_name ='LSadmin/sidebar.html'
    
    
class Addperson(TemplateView):
    template_name ='LSadmin/add-person.html'
    success_url = "/Uapp/login2.html/"
    
    
class Manageperson(TemplateView):
    template_name ='LSadmin/manage-person.html'
    success_url = "/Uapp/login2.html/"
    
class Managerdashboard(TemplateView):
    template_name='user/manager_dashboard.html'
    
class Base(TemplateView):
    template_name='LSadmin/base.html'