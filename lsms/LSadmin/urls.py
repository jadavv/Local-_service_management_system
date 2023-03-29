from django.urls import path,include
from Uapp import views
from .views import AdminLoginView,Dashboardmanage,Sidebarmanage,Addperson,Base,Manageperson

urlpatterns = [
   path('login/',AdminLoginView.as_view(),name='login'),
   path('dashboard/',Dashboardmanage.as_view(),name='dashboard'),
   path('sidebar/',Sidebarmanage.as_view(),name='sidebar'),
   path('addperson/',Addperson.as_view(),name='add-person'),
   path('base/',Base.as_view(),name='base'),
   path('manageperson/',Manageperson.as_view(),name='manage-person')
]
