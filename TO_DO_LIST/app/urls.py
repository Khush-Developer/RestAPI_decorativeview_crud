from django.urls import path
from . import views

urlpatterns = [
            path('', views.Homeview, name='home'),
            path('detail/<str:pk>', views.DetailView, name='detail'),
            path('create/', views.CreateView, name='create'),
            path('updateview/<str:pk>', views.UpdateView, name='updateview'),
            path('delete/<str:pk>', views.DeleteView, name='delete'),
        ]