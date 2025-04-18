# urls.py do seu app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sqli/', views.sqli_lab, name='sqli'),  # Nova URL
    path('xss/', views.xss_lab, name='xss'),     # Nova URL
    path('sqli-details/', views.sqli_details, name='sqli_details'),
    path('xss-details/', views.xss_details, name='xss_details'),

    
]
