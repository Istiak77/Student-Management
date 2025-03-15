from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView

urlpatterns = [

    path('', StudentListView.as_view(), name='index'),
    path('add/', StudentCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
]