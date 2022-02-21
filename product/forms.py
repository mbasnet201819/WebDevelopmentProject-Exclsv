from django import forms
from product.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
