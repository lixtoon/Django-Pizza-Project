from django.contrib import admin
from django.urls import path
from .views import userlogout, userauthenticate, customerwelcomeview, userloginview, adminloginview,adminhomepageview, authentificateadmin, logoutadmin, addpizza, deletepizza, editpizza, editedpizza, backpage, homepageview, signupuser


urlpatterns = [
    path('admin/',adminloginview, name='adminloginpage'),
    path('adminauthentificate/', authentificateadmin),
    path('adminlogout/', logoutadmin),
    path('pageback/', backpage),
    path('admin/homepage/',adminhomepageview, name='adminhomepage'),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('editpizza/<int:pizzapk>/', editpizza),
    path('editpizza/<int:pizzapk>/update/', editedpizza),
    path('signupuser/',signupuser),
    path('',homepageview, name='homepage'),
    path('loginuser/',userloginview, name= 'userloginpage'),
    path('customer/welcome/',customerwelcomeview,name= 'customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/', userlogout)
]
