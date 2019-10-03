
from django.urls import path
from . import views



urlpatterns = [


    path('', views.ClickPost),
    path('m/', views.music, name='welcome')
]