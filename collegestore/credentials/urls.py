from . import views
from django.urls import path

urlpatterns = [

    path('Register', views.register, name='Register'),
    path('Login', views.login, name='Login'),
    path('new', views.new, name='new'),
    path('logout',views.logout,name='logout')
]