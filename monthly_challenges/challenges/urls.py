from django.urls import path
from . import views

urlpatterns = [    
    path('<int:month>', views.monthly_challenge_by_number),    # if integers
    path('<str:month>', views.monthly_challenge),    # if string
]