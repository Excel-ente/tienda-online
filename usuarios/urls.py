from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.status, name='auth_status'),
    path('register/', views.register, name='auth_register'),
    path('login/', views.login_view, name='auth_login'),
    path('logout/', views.logout_view, name='auth_logout'),
]
