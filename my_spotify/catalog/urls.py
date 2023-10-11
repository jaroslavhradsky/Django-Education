from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list),
    path('album/<int:id>', views.album),

]