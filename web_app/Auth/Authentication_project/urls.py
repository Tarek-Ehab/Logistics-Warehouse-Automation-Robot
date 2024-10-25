"""Authentication_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Accounts.urls')),
    
    
    path('addbuyer/', views.addbuyer, name='addbuyer'),
    path('addcarDrop/', views.addcarDrop, name='addcarDrop'),
    path('addclassification/', views.addclassification, name='addclassification'),
    path('addorder/', views.addorder, name='addorder'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('addshelf/', views.addshelf, name='addshelf'),
    path('addsupplier/', views.addsupplier, name='addsupplier'),
    path('addZone/', views.addZone, name='addZone'),
    path('buyer/', views.buyer, name='buyer'),
    path('carDrop/', views.carDrop, name='carDrop'),
    path('classification/', views.classification, name='classification'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('productList/', views.productList, name='productList'),
    path('productsBuyer/', views.productsBuyer, name='productsBuyer'),
    path('productsByClass/', views.productsByClass, name='productsByClass'),
    path('ProductsBySupplier/', views.ProductsBySupplier,
         name='ProductsBySupplier'),
    path('productsZone/', views.productsZone, name='productsZone'),
    path('shelf/', views.shelf, name='shelf'),
    path('supplier/', views.supplier, name='supplier'),
    path('updatebuyer/', views.updatebuyer, name='updatebuyer'),
    path('updatecardrop/', views.updatecardrop, name='updatecardrop'),
    path('updateclassification/', views.updateclassification,
         name='updateclassification'),
    path('updatedelivery/', views.updatedelivery, name='updatedelivery'),
    path('updateorder/', views.updateorder, name='updateorder'),
    path('updateproduct/', views.updateproduct, name='updateproduct'),
    path('updateshelf/', views.updateshelf, name='updateshelf'),
    path('updatesupplier/', views.updatesupplier, name='updatesupplier'),
    path('updateZone/', views.updateZone, name='updateZone'),
    path('user/', views.user, name='user'),
    path('zone/', views.zone, name='zone'),

]
