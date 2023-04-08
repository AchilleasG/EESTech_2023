from .models import *
from django import forms

'''class Simple_Product_Login(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':"Enter name for product"}))

    def save(self):
        product = []
        try:
            product = Product.objects.get(name__iexact=self.cleaned_data.get("name"))

        except :
            Product.objects.create(name=self.cleaned_data.get("name"))
            product = Product.objects.get(name__iexact=self.cleaned_data.get("name"))

        return product
    
    '''