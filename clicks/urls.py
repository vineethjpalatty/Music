
from django.urls import path
from . import views



urlpatterns = [


    path('', views.ClickPost,name='home'),
    path('m/', views.music, name='welcome')
]