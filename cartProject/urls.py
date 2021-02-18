"""cartProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/',views.product_view),
    path('cart_add/',views.cart_add_view),
    path('cart_show/',views.cart_show_view),
    path('signup/',views.signup_view,name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete/<int:pk>',views.delete_view,name="deletedata"),
    path('get_price/',views.get_price),
    path('',views.home_view)
]
