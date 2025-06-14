from django.urls import path
from . import views

urlpatterns = [    
    path('v1/listCountries/', views.listCountries),
    # path('v1/signup/', views.signup),
    # path('v1/login/', views.login),
    # path('v1/logout/', views.logout),
]