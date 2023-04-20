from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [   
    path("",views.home1,name="home1"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("secondsign/",views.secondsign,name="secondsign")
]