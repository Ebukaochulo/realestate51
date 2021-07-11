from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('property-grid/', views.property_grid, name='property-grid'),
    path('property-single/<str:pk>/', views.property_single, name='property-single'),
    path('contact', views.contact, name='contact'),
    path('', views.home, name='index'),
    path('search/', views.search, name='search'),
    
]
