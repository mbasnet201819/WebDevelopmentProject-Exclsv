from django.contrib import auth
from django.shortcuts import render, redirect

from exclusive.forms import CustomerForm
from exclusive.models import Customer
from product.models import Product


def Index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        name = request.POST["name"]
        password = request.POST["password"]
        try:
            customer = Customer.objects.get(username=name, password=password)
            return redirect('Main')


        except:
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                return redirect('show')
            return render(request, 'Main/Main.html')

    else:
        form = CustomerForm()
        return render(request, 'login.html', {'form': form})


def show(request):
    pro = Product.objects.all()
    cus = Customer.objects.all()
    return render(request, "administator/admin.html", {'products': pro, })


def cust(request):
    cus = Customer.objects.all()
    return render(request, "administator/customer.html", {'customer': cus})


def signup(request):
    if request.method == "POST":
        if request.method == "POST":
            print(request.POST)
            form = CustomerForm(request.POST)
            form.save()
            return redirect('login')
        else:
            form = CustomerForm()
        return render(request, "administator/admin.html", {'form': form})
    return render(request, "register.html")


def logout(request):
    request.session.clear()
    return redirect('index')


def signin(request):
    return render(request, "login.html")


def cdelete(request, p_id):
    u = Customer.objects.get(id=p_id)
    u.delete()
    return redirect("/show")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Product.objects.filter(productname__contains=searched)
        return render(request, "administator/admin.html", {'searched': searched, 'items': items})
    else:
        return render(request, "administator/admin.html")


def searchproduct(request):
    return redirect("/show")


def Main(request):
    return render(request, "Main/Main.html")
