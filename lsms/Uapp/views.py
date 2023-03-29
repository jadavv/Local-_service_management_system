from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ServiceProviderRegisterForm,CustomerRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.


class ServiceProviderRegisterForm(CreateView):
    model=User
    form_class =ServiceProviderRegisterForm
    template_name= 'Uapp/service_register.html' 
    success_url ="/Uapp/login/"
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] ='service'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class CustomerRegisterForm(CreateView):
    model=User
    form_class =CustomerRegisterForm
    template_name='Uapp/customer_register.html'
    success_url ="/Uapp/login/"
    
    
    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'customer'
        return super().get_context_data(**kwargs)
    
class UserLoginView(LoginView):
    template_name= 'Uapp/login2.html'
    success_url ="/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_servicer:
                return '/Uapp/DashboardView/'
            else:
                return '/Uapp/DashboardView/'
            

class ServiceDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()
        
        return render(request, 'user/manager_dashboard.html',{
            'projects':project,
        })

    template_name = 'user/manager_dashboard.html'
    
class CustomerDashBoardView(ListView):
    
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    
    template_name = 'project/project_list.html'
    
    
 
class AdminRegisterView(CreateView):
    model = User
    form_class = CreateView
    template_name = 'LSadmin/admin_login.html'
    success_url = "/"   
    
            
    
class IndexViewPage(TemplateView):
    template_name = 'Uapp/index.html'
    
class DashboardView(TemplateView):
    template_name ='admin/dashboard.html'
    
    
class RegisterPage(TemplateView):
    template_name ='Uapp/register.html'
    success_url = "/Uapp/login2.html/"
    
    
class Navbar(TemplateView):
    template_name ='user/Navbar.html'
    success_url = "/Uapp/login2.html/"
    
class Managerdashboard(TemplateView):
    template_name='user/manager_dashboard.html'
    
class Base(TemplateView):
    template_name='user/base.html'