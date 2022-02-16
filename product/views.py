from django.shortcuts import render, redirect

from product.forms import ProductForm
from product.models import Product


def create(request):  # add product page
    return render(request, 'administator/addproduct.html')


def product_create(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/create")
    else:
        form = ProductForm()
    return render(request, "administator/admin.html", {'form': form})


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
