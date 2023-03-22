from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ServiceProviderRegisterForm,CustomerRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


class ServiceProviderRegisterForm(CreateView):
    model=User
    form_class =ServiceProviderRegisterForm
    template_name= 'Uapp/service_register.html' 
    success_url ="/"
    
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
    success_url ="/"
    
    
    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'customer'
        return super().get_context_data(**kwargs)
    
class UserLoginView(LoginView):
    template_name= 'Uapp/login2.html'
    success_url ="/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_servicer:
                return '/Uapp/profile/'
            else:
                return 'customer'
class profileTemplateView(TemplateView):
    template_name ='Uapp/index.html'
    
    
class RegisterPage(TemplateView):
    template_name ='Uapp/register.html'