from django.shortcuts import render,redirect
from testapp.forms import ProductForm , CartForm ,SignupForm
from testapp.models import Cart,Product
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def product_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return  redirect("/")
    return  render(request,'testapp/product.html',{'form':form})

@login_required
def cart_add_view(request):
    form = CartForm()
    #form.fields['price'].widget.attrs['disabled'] = True
    if request.method == 'POST':
        form = CartForm(request.POST,request=request)
        if form.is_valid():
            form.instance.user = request.user
            name = request.POST.get('name')
            try:
                q1 = Cart.objects.get(user=request.user, name=name)
            except Cart.DoesNotExist:
                q1 = None
            if q1 == None:
                form.save(commit=True)
            return redirect("/")
    return  render(request,'testapp/Cart.html',{'form':form})

@login_required
def cart_show_view(request):
    data = Cart.objects.filter(user=request.user)
    total = 0
    for item in data:
        total = total + item.quantity * item.price

    return render(request,'testapp/cart_show.html',{'cart_item':data,'total':total})


def delete_view(request,pk):
    item = Cart.objects.get(id=pk)
    item.delete()
    return redirect("/")

def get_price(request):
    if request.method == 'GET':
        item_name = request.GET['item_name']
        data = Product.objects.get(product_name=item_name)

        return HttpResponse(data.price)

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        #if form.is_valid():
            #form.save(commit =True)
        return redirect('/accounts/login')
    return render(request,'registration/signup.html',{'form':form})

def home_view(request):
    return render(request,'testapp/base.html')