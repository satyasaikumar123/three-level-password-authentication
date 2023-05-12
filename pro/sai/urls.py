from django.contrib import admin
from django.urls import path
from .import views 
from django.urls import path
from .views import reset_password
from django.contrib.auth import views as auth_views





urlpatterns = [   
    path("",views.home1,name="home1"),
    path("Home",views.Home,name="Home"),
    path("signup/",views.signup,name="signup"),
    path("register1/", views.register1, name="register1"),
    path("login/",views.login,name="login"),
    path("login1/",views.login1,name="login1"),
    path('login_with_otp/',views.login_with_otp, name='login_with_otp'),
    path("logout/",views.logout,name="logout"),
    path('reset_password/', reset_password, name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   
]