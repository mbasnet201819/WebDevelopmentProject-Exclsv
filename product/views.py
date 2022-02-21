from django.shortcuts import render, redirect

from product.forms import ProductForm, OrderForm
from product.models import Product, Order


def create(request):  # add product page
    return render(request, 'administator/addproduct.html')


def order(request):  # add product page
    ord = Order.objects.all()
    return render(request, 'administator/orders.html', {'order': ord})


def product_create(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/order")
    else:
        form = ProductForm()
    return render(request, "administator/admin.html", {'form': form})


def order_create(request):
    if request.method == "POST":
        print(request.POST)
        form = OrderForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("Sale")
    else:
        form = OrderForm()
    return render(request, "Main/payment.html", {'form': form})


def Sale(request):
    p = Product.objects.all()
    return render(request, "Main/Product.html", {'product': p})


def pupdate(request, p_id):
    order = Product.objects.get(id=p_id)
    form = ProductForm(instance=order, )
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/show")
    context = {'form': form}
    return render(request, "administator/update.html", context)


def pdelete(request, p_id):
    product = Product.objects.get(id=p_id)
    product.delete()
    return redirect("/show")


def odelete(request, p_id):
    order = Order.objects.get(id=p_id)
    order.delete()
    return redirect("/order")
