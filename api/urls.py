from django.urls import path
from . import views

urlpatterns = [    
    path('v1/signup/', views.signup),
    path('v1/login/', views.login),
    path('v1/logout/', views.logout),
    path('v1/listUsers/', views.listUsers),
    path('v1/listCountries/', views.listCountries),
    path('v1/listTasks/', views.listTasks),
    path('v1/zonesCountry/', views.zonesCountry),
    path('v1/hourZone/', views.hourZoneCountry),            
]