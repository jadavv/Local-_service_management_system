from django.contrib import admin
from django.urls import path,include
from .views import ServiceProviderRegisterForm,CustomerRegisterForm,UserLoginView,AdminRegisterView,CustomerDashBoardView,ServiceDashboardView
from django.contrib.auth.views import LogoutView
from Uapp import views


urlpatterns = [

    path('serviceregister/',ServiceProviderRegisterForm.as_view(),name='serviceregister'),
    path('adminlogin/',AdminRegisterView.as_view(),name='admin_login'),
    path('customerregister/',CustomerRegisterForm.as_view(),name='customerregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('DashboardView/',views.DashboardView.as_view(),name='DashboardView'),
    path('manager_dashboard/',ServiceDashboardView.as_view(),name='manager_dashboard'),
    path('developer_dashboard/',CustomerDashBoardView.as_view(),name='developer_dashboard'),
    path('register/',views.RegisterPage.as_view(),name='register'),
    path('index/',views.IndexViewPage.as_view(),name='Index'),
    path('Navbar',views.Navbar.as_view(),name='Navbar'),
    path('managerdashboard',views.Managerdashboard.as_view(),name='manager_dashboard'),
    path('base',views.Base.as_view(),name='Base'),
]