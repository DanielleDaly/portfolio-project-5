from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_enquiry, name='customer_enquiry'),
    # path('add/', views.add_customer_enquiry, name='add_customer_enquiry'),
]