from django import forms
from exclusive.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

