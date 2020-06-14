from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel
# Create your views here.

def adminloginview(request):
    return render(request, "adminlogin.html")

def authentificateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password= password)
    if user is not None and user.username=='admin':
        login(request,user)
        return redirect('adminhomepage')
    if user is None:
        messages.add_message(request,messages.ERROR, 'invalid credentials')
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'pizzas' : PizzaModel.objects.all()}
    return render(request,"adminhomepage.html", context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    pname = request.POST['pizzaname']
    pprice = request.POST['pizzaprice']
    PizzaModel(name=pname, price=pprice).save()
    return redirect('adminhomepage')

def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id = pizzapk).delete()
    return redirect('adminhomepage')

def editpizza(request, pizzapk):
    context = {'pizzapk':pizzapk}
    return render(request, "editpizza.html", context)

def editedpizza(request, pizzapk):
    namepizza = request.POST['pizzaname']
    pricepizza = request.POST['pizzaprice']
    mypizza = PizzaModel.objects.filter(id = pizzapk)[0]
    mypizza.name = namepizza
    mypizza.price = pricepizza
    mypizza.save()
    return redirect('adminhomepage')

def backpage(request):
    return redirect('adminhomepage')

def homepageview(request):
    return render(request, "homepage.html")
    pass
