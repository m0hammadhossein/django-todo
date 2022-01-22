from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('edit/<int:pk>/', views.Edit.as_view(), name='edit'),
    path('view/<int:pk>/', views.ViewDetail.as_view(), name='view'),
    path('create/', views.CreateTask.as_view(), name='create')

]
