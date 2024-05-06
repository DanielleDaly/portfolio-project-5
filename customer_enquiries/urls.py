from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_enquiry, name='customer_enquiry'),
]