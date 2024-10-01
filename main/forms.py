from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category","price"]

#CSS
