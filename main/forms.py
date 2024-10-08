from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category","price"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)


#CSS
