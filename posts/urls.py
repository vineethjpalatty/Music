
from django.urls import path
from .import views


urlpatterns = [

    path('e/',views.BlogView1,name='home'),
    path('b/', views.BlogView2),
    path('c/', views.BlogView3),
    path('d/', views.BlogView4),
    path('',views.Blog.as_view()),

]
