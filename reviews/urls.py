from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('<int:review_id>/', views.review, name='review'),
]