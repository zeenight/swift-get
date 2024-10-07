from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category","price"]

#CSS
