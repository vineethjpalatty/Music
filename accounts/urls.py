from django.urls import path
from . import views





urlpatterns = [
    path('signup/', views.signup1.as_view(), name='signup'),

]