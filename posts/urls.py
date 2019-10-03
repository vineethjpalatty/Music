
from django.urls import path
from .import views

urlpatterns = [

    path('upload/',views.Blog.as_view(),name='upload'),
    path('display/', views.BlogView2,name='display'),


]

