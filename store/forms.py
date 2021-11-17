from django import forms
from django.forms import fields
from .models import Product

       
class StoreCreateForm(forms.ModelForm):
    class Meta:
        model =Product
        fields=['category','name','price','image']
        
class StoreSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required =False)
    class Meta:
        model = Product
        fields = [ 'name']
        
