from django.urls import path
from . import views

urlpatterns = [
    path('print/', views.print_notes, name='print_notes'),
    path('print/<int:id>/', views.print_single_note, name='print_single_note'),
]
