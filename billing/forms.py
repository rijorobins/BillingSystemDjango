from django import forms
from django.forms import ModelForm
from billing.models import Product,Purchase
class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name"]
class AddPurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["product","quantity","purchase_price","selling_price"]
