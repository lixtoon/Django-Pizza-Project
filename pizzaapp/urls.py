from django.contrib import admin
from django.urls import path
from .views import adminloginview,adminhomepageview, authentificateadmin, logoutadmin, addpizza, deletepizza, editpizza, editedpizza, backpage, homepageview


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
    path('',homepageview),
]
