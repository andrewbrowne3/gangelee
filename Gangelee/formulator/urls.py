from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('Products',views.ProductsPage,name='products'),
   path('ProductInfo/<str:pk>/',views.ProductInformation,name='productinfo'),
   path('Formulation/<str:pk>/',views.FormulationInformation ,name='formulationpage'),
]
