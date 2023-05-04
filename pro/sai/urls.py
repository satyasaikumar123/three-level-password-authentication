from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [   
    path("",views.home1,name="home1"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("login/home1.html",views.home1,name="home1"),
     path("login1/",views.login1,name="login1"),
    # path("register1/",views.register1,name="register1"),
    # path("register1/<str:username>/", veiws.register1, name='register1'),
    path("register1/", views.register1, name="register1"),
    path("logout/",views.logout,name="logout"),
    
]