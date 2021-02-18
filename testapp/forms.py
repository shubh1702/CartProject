from django import forms
from testapp.models import Product, Cart
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ('user',)
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    username = None
    def __init__(self, *args, request=None, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.request = request
        if request is not None:
            global username
            username = request.user

    def clean(self):
        total_cleaned_data = super().clean()
        name = total_cleaned_data['name']
        quantity = total_cleaned_data['quantity']
        user = username
        try:
            q1 = Cart.objects.get(user=user, name=name)
        except Cart.DoesNotExist:
            q1 = None
        if q1 != None:
            q1.quantity = q1.quantity + quantity
            q1.save()

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
        }