from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='url-list'),
    path('album/<int:id>', views.album, name='url-album'),

]