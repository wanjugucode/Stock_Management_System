from django import forms
from store.models import Product


class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class StoreCreateForm(forms.ModelForm):
    class Meta:
        model =Product
        fields=['category','name','price','image']


    
