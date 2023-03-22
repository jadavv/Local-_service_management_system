from django.contrib import admin
from django.urls import path,include
from .views import ServiceProviderRegisterForm,CustomerRegisterForm,UserLoginView
from django.contrib.auth.views import LogoutView
from Uapp import views


urlpatterns = [

    path('serviceregister/',ServiceProviderRegisterForm.as_view(),name='serviceregister'),
    path('customerregister/',CustomerRegisterForm.as_view(),name='customerregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',views.profileTemplateView.as_view(),name='profile'),
    path('register/',views.RegisterPage.as_view(),name='register.html')
]