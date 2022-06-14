from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.request_login, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('timeline/<int:user>', views.timeline, name='timeline'),
    path('follow', views.follow, name='follow'),
    path('officers', views.officers, name='officers'),
]